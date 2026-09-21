# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/6dyNreOMuOAenymg0Owm8A
# Reader base: https://docs.blackduck.com/r/srm/latest/
# Captured: 2026-09-21



===== TOPIC: Correlation Overview =====
# URL: https://docs.blackduck.com/r/srm/latest/ (topic id LOwf~~7xnx9CF2dY5ANsMA)

Correlation is the process Software Risk Manager uses to evaluate data returned by any
                        combination of supported AppSec tools to determine which, if any, of the
                        results reported by the various tools refers to the same issue. When
                        matching results are found, Software Risk Manager correlates those results and creates a
                        single finding for that issue. Software Risk Manager does this by looking at the data
                        provided for each result; although, in some cases, the correlation process
                        will factor in the detection method as well (e.g., Static vs. Dynamic
                        results).

                Correlation involves various processes that check for data within results that
                        would suggest whether results should be correlated. The output is a
                        per-result set of associations, where each association indicates whether to
                        allow or deny correlation. At the end of this process, the correlation
                        decisions for all results are used to determine which results have enough
                        evidence to be grouped into the same finding. (For more information, see
                        Analysis Correlation Options.)

                The correlation process includes the following elements:
                                Rule Sets

                                Data
                                                Normalization

                                Location-based Correlation

                                Component
                                                Correlation

                                Hybrid
                                                Correlation

                                InfraSec
                                                Correlation

                                Location-less Correlation


===== TOPIC: Understanding Component Correlation =====
# URL: https://docs.blackduck.com/r/srm/latest/ (topic id 2E7Urfdu5XzSCnB2kx0Jag)

There are five ways to correlate components (for more information, see Analysis Correlation Options). Component correlation modes control how
            Software Component Analysis (SCA) tool results are correlated to findings. SRM can be
            configured to correlate component results using different combinations of the following data:
                vulnerability (e.g., BDSA-2021-0069, CVE-2021-24122)

                component name and version (e.g., Spring Framework version 3.2.4)

                type (e.g., Vulnerable Component)

                component identifier (e.g., org.springframework:spring-aop:3.2.8.RELEASE)

            

        You will get one finding per unique set of values for each option. For example, selecting
            "vulnerability, component name/version, and type" will result in a finding for each
            vulnerability for each component and type that you have. However, if "vulnerability and
            type" is selected, you will only get a finding per vulnerability and type that covers
            all components. The default mode is "vulnerability, component identifier, and type."


===== TOPIC: Understanding Hybrid (SAST/DAST) Correlation =====
# URL: https://docs.blackduck.com/r/srm/latest/ (topic id 71bvl9S44aScgR3WWzZHow)

When Hybrid Correlation is enabled, URL-located results may be correlated with
            file-located results by mapping result URLs to a set of source code locations. Results
            with file and URL locations may be correlated if the file location overlaps with any of
            the discovered file locations for the given URL. (Data flows are also checked for
            overlaps.)

        Source code is analyzed (for supported languages
            and frameworks) to determine the specific files and line ranges that declare the
            endpoint used by the URL path. If binaries are also provided, Software Risk Manager will
            automatically build a call graph from the indicated source location to collect
            additional locations to compare against. (Call graph generation is only
            supported for JVM and CLR binaries.)


===== TOPIC: Agentless Correlation =====
# URL: https://docs.blackduck.com/r/srm/latest/ (topic id 265ep8Qv6JfX~u8eeCezvQ)

Agentless correlation uses a static analysis approach on source code and binaries to
            correlate SAST and DAST results. No configuration steps are required to make use of
            agentless correlation. The only requirement is uploading source code at some point
            in an analysis.

        
    

    Correlation Performance Impact

        Agentless Correlation greatly expands the set of possibilities that must be considered to create
                a hybrid finding. Since exact code paths aren't provided, many inferred paths are
                created and evaluated during correlation. This can greatly impact the speed of
                correlation during analysis.

    

    Requirements and Known Limitations

        For information on requirements and known limitations, see the following topics:
                Requirements.

                Known
                            Limitations.


===== TOPIC: Agentless Correlation Known Limitations =====
# URL: https://docs.blackduck.com/r/srm/latest/ (topic id fmuclRdMo9y2HQ9hfNjUfQ)

Agentless Correlation explores a set of possible execution paths from an endpoint to find
            correlations with a code location. These explored paths may be inactive or incomplete
            due to undetected endpoints, inheritance and strategy patterns, anonymous functions, or
            other features for a given language and web framework.


===== TOPIC: Integrations Overview =====
# URL: https://docs.blackduck.com/r/srm/latest/ (topic id vrBwAiA9qsLHOV_6~ExBAg)

Click the Integrations icon in the navigation bar to open the Integrations page.

        
            

        

        The default view lists all the currently configured integration tools.

        
            Use the menu on the left to display supported tools arranged by tool type.

            Select All to display all the analysis tools, integration tools, IDEs, issue
                tracking systems, plugins, and version control tools supported by SRM.

            Select Configured to display all the currently configured integration tools.

            Enter a search term in the Search Integrations field to search for a specific
                tool.

        

    

    Integration Tool Types

        
        
            SRM supports the following types. (Click the link for additional information.)
                    Analysis Tools

                    Continuous Integration

                    Integrated Development
                            Environments

                    Issue Tracking

                    Plugins

                    Source Code Management

                

            Analysis Tools

                
                SRM supports the following Analysis Tools:

                
                    42Crunch

                    Acunetix Desktop (XML)

                    Acunetix 360

                    Anchore (JSON)

                    Android Lint (XML)

                    APIsec

                    AppScan DAST (XML)

                    AppScan Enterprise

                    AppScan Source (OZASMT)

                    AppSpider (XML)

                    Aqua Enterprise

                    Arachni (JSON and XML)

                    Armorize CodeSecure (XML)

                    ASoC (XML)

                    AWS Security Hub (JSON)

                    Azure Security Center (CSV)

                    Black Duck SCA

                    Black Duck Binary Analysis (CSV and JSON)

                    Brakeman (JSON and ZIP of JSON outputs) (Built-in tool)

                    Burp Enterprise

                    Burp Suite (XML)

                    C++test (XML)

                    CAST Highlight

                    CAT.NET (XML) (Built-in tool)

                    Checkmarx (XML)

                    Checkmarx IAST

                    Checkmarx One

                    Checkstyle (XML) (Built-in tool)

                    Clang (ZIP of HTML outputs)

                    Clang-Tidy (TXT: console log)

                    Clippy (JSON and ZIP of JSON outputs) (Built-in tool)

                    CodePeer (CSV)

                    CodeSonar (CodeSonar-Scrape ZIP)

                    Continuous Dynamic (formerly WhiteHat)

                    Contrast

                    Coverity (JSON v8+)

                    Coverity on Polaris

                    Cppcheck (XML v2) (Built-in tool)

                    CycloneDX (JSON and XML)

                    Data Theorem Mobile

                    DefenseCode ThunderScan (JSON)

                    Defensics Fuzz Test (XML: super-summary.xml)

                    Dependency-Check (XML) (Built-in tool)

                    Dependency-Track

                    dotTEST (XML)

                    Dynatrace

                    ErrCheck (TXT: console.log)

                    error-prone (TXT)

                    ESLint (JSON) (Built-in tool)

                    Faraday

                    Fortify (FPR)

                    Fortify Software Security Center

                    FxCop (XML and ZIP of XML outputs) (Built-in tool)

                    Gendarme (XML) (Built-in tool)

                    GitHub Advanced Security

                    GitLab Security (JSON) and Report (ZIP)

                    GoCyclo (TXT: console log)

                    Google SCC

                    GoLint (TXT: console log)

                    GoSec (JSON)

                    Grype (JSON)

                    Hacker One

                    Harbor (JSON and CSV)

                    Helix PRQA-QAC (CSV)

                    Imperva

                    IneffAssign (TXT: console log)

                    Inviciti (XML)

                    Inviciti Enterprise (XML: Vulnerabilities List)

                    IriusRisk

                    JFrog Xray (JSON)

                    Jlint (TXT)

                    JSHint (TXT) (Built-in tool)

                    Jtest (TXT) (Built-in tool)

                    Mend SCA

                    Microsoft Defender For Cloud

            
                    Microsoft Code Analysis (TXT: MSBuild log and TSV: errors table)

                    Microsoft Threat Model (HTM and TM7)

                    MobSF (JSON: Generate JSON Report endpoint)

                    MobSF Scan (JSON)

                    NDepend (XML)

                    Nessus (NESSUS)

                    NeuVector

                    Nmap (XML)

                    NowSecure 

                    NowSecure Workstation (JSON and ZIP of JSON outputs)

                    OCLint (XML)

                    Orca Security

                    PHP_CodeSniffer (XML) (Built-in tool)

                    PHPMD (XML) (Built-in tool)

                    PMD (XML) (Built-in tool)

                    Polaris

                    Prisma Cloud (RedLock) (CSV and JSON: List Alerts V1 endpoint)

                    Prisma Cloud Compute (Twistlock) (CSV and JSON)

                    Pylint (JSON and ZIP of JSON outputs)

                    Q-MAST

                    Qualys CS (CSV)

                    Qualys VM (XML)

                    Qualys VMDR

                    Qualys WAS

                    Rapid Scan SAST (JSON)

                    Rapid7 InsightAppSec

                    Rapid7 Nexpose (XML)

                    SafeSQL (TXT: console log)

                    SARIF (JSON v2.1.0)

                    SATE (XML)

                    Scalastyle (XML) (Built-in tool)

                    SCAP (XML)

                    SciTools Understand (CSV)

                    SD Elements

                    Black Duck Seeker

                    Semgrep (JSON)

                    Snyk (JSON)

                    SonarQube

                    Sonatype Nexus

                    SPDX (JSON and SPDX)

                    SpotBugs (XML) (Built-in tool)

                    SRM Custom Integration (XML)

                    Staticcheck (JSON)

                    STIG (CKL, CKLB)

                    SWAMP (XML)

                    Black Duck Managed Services Platform (XML)

                    Tenable.io

                    Tenable.io Web App Scanning

                    Tenable.sc

                    Black Duck Tinfoil API

                    Black Duck Tinfoil Web

                    Trivy (JSON: container image results)

                    TruffleHog (JSON)

                    Trustwave App Scanner

                    Veracode (XML and ZIP)

                    Vet (JSON)

                    WebInspect (XML)

                    Wiz

                    WPScan (JSON)

                    ZAP (XML)

                    ZPA (JSON) (Built-in tool)

                

            

            Continuous Integration

                
                
                SRM supports the following CI tools (click the link for more information):
                        Bamboo

                        GitHub
                                Action

                        Jenkins

                        Black Duck SRM
                                API

                        Black Duck Bridge CLI

                        TeamCity

                    

            

            Integrated Development Environments

                
                
                SRM supports the following IDEs (click the link for more information):
                        Code
                                Sight IntelliJ

                        Code
                                Sight Visual Studio Code

                        Eclipse

                        Visual Studio

                    

            

            Issue Tracking

                
                
                SRM supports the following issue tracking tools (click the link for more
                        information):
                        Azure
                                DevOps

                        GitHub

                        GitLab

                        Jira

                        ServiceNow

                    

            

            Plugins

                
                SRM supports the following plugins (click the link for more information):
                        Burp

                        Splunk

                        ZAP

                    

            

            Source Code Management

                
                
                SRM supports the following SCM systems (click the link for more information):
                        Git
