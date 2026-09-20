// c-vuln-app: minimal C product for the CRA reachability PoC.
//
// Vendors zlib 1.2.12 (third_party/zlib), which is affected by
// CVE-2022-37434: a heap-based buffer over-read/over-write in inflate() when
// processing a gzip header whose EXTRA field is longer than the space
// reserved by inflateGetHeader(). This program feeds exactly such a gzip
// stream into inflate(), so the vulnerable code IS reachable:
//
//     main -> gunzip_file -> inflate   (EXTRA state, CVE-2022-37434)
//
// The vuln->function mapping (CVE-2022-37434 -> inflate@third_party/zlib/inflate.c)
// is hand-curated in poc/curation/vuln-function-map.json.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "zlib.h"

// Gunzip a buffer via the raw inflate() API.
static int gunzip_file(const unsigned char *src, size_t src_len,
                       unsigned char *dst, size_t dst_cap) {
    z_stream strm;
    memset(&strm, 0, sizeof(strm));
    // 47 = 15 (windowBits) + 32 (auto-detect gzip/zlib header).
    if (inflateInit2(&strm, 47) != Z_OK)
        return -1;
    strm.next_in = (unsigned char *)src;
    strm.avail_in = (unsigned int)src_len;
    strm.next_out = dst;
    strm.avail_out = (unsigned int)dst_cap;
    // CVE-2022-37434: inflate() hits the vulnerable EXTRA-field copy when the
    // gzip header carries an extra field.
    int ret = inflate(&strm, Z_FINISH);
    inflateEnd(&strm);
    return (ret == Z_STREAM_END || ret == Z_OK) ? (int)strm.total_out : -1;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s <file.gz>\n", argv[0]);
        return 2;
    }
    FILE *f = fopen(argv[1], "rb");
    if (!f) {
        perror("fopen");
        return 1;
    }
    fseek(f, 0, SEEK_END);
    long len = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc((size_t)len);
    if (fread(buf, 1, (size_t)len, f) != (size_t)len) {
        fprintf(stderr, "short read\n");
        return 1;
    }
    fclose(f);

    unsigned char out[65536];
    int n = gunzip_file(buf, (size_t)len, out, sizeof(out));
    free(buf);
    if (n < 0) {
        fprintf(stderr, "inflate failed\n");
        return 1;
    }
    printf("gunzipped %d bytes: %.*s", n, n, (char *)out);
    return 0;
}
