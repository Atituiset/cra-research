// go-vuln-app: minimal Go product for the CRA reachability PoC.
//
// It carries two vulnerable dependencies on purpose:
//
//   - golang.org/x/crypto v0.16.0: CVE-2023-48795 (Terrapin) lives in the SSH
//     handshake path. ssh.Dial below drives execution straight into it, so the
//     vulnerable code IS in the execute path -> VEX "affected".
//   - golang.org/x/net v0.19.0: CVE-2023-45288 / GO-2024-2687 live in
//     x/net/http2, which this program never imports. Only x/net/idna is used,
//     so the vulnerable code is NOT in the execute path -> VEX "not_affected".
package main

import (
	"fmt"

	"golang.org/x/crypto/ssh"
	"golang.org/x/net/idna"
)

// connectSSH dials an SSH server. The client handshake in x/crypto/ssh
// v0.16.0 is the Terrapin-vulnerable code path (CVE-2023-48795).
func connectSSH(addr string) error {
	cfg := &ssh.ClientConfig{
		User:            "poc",
		Auth:            []ssh.AuthMethod{ssh.Password("poc")},
		HostKeyCallback: ssh.InsecureIgnoreHostKey(), // PoC only
	}
	// ssh.Dial enters the vulnerable handshake code immediately.
	conn, err := ssh.Dial("tcp", addr, cfg)
	if err != nil {
		return err
	}
	return conn.Close()
}

func main() {
	// x/net is only exercised through idna — the vulnerable http2 package is
	// never reached.
	ascii, err := idna.Lookup.ToASCII("münchen.de")
	if err != nil {
		panic(err)
	}
	fmt.Println("idna:", ascii)

	if err := connectSSH("127.0.0.1:22"); err != nil {
		fmt.Println("ssh dial (expected to fail without a server):", err)
	}
}
