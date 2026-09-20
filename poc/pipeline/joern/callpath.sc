// Joern script: dump method definitions and call edges as TSV lines.
// Consumed by poc/pipeline/reach_c.py, which reconstructs call paths in Python.
// Run: joern --script callpath.sc --param cpgFile=/out/cpg.bin
@main def exec(cpgFile: String) = {
  importCpg(cpgFile)
  cpg.method.l.foreach { m =>
    if (!m.isExternal) {
      println(s"DEF\t${m.name}\t${m.fullName}\t${m.filename}\t${m.lineNumber.getOrElse(-1)}")
    }
  }
  cpg.call.l.foreach { c =>
    val caller = c.method.fullName
    val line = c.lineNumber.getOrElse(-1)
    val file = c.file.name.headOption.getOrElse("")
    println(s"CALL\t$caller\t${c.name}\t${c.methodFullName}\t$line\t$file")
  }
}
