# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q
# Reader base: https://docs.blackduck.com/bundle/blackduck-hub/page/
# Captured: 2026-09-21



===== TOPIC: About Signature Scanning =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id t_RBmGxhHIiFCDcy_iv6eQ)




===== TOPIC: About Reduced Persistence Signature Scanning =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id 0FAJZum7LZ_eQkteExzPIQ)

In the source view, many users rarely look at unmatched files from signature scanning, but all of that data is by far the biggest consumer of space in the database. Performance testing also shows that inserting the file data into the database is a significant fraction of scan time.

Reduced Persistence Signature Scanning aims to decrease database size and growth and also increase scan performance by no longer saving data for files that are not matched by signature scanning. However, if your use case requires that unmatched file data be saved, there are settings to retain that data available at the global, project, and/or scan levels.

There is also the option to purge existing unmatched files to further reduce database disk usage.

Settings
Unmatched files are no longer retained by default. However, retention policy can be changed.

Global setting. In System Settings under Data Retention, there is an option to enable retention of unmatched files. When it is not enabled (the default), there is an option to purge all existing unmatched files from all projects. The option to purge is not presented if retention is enabled. Note that the global setting only applies to projects and scans that do not explicitly specify their own setting; similarly, changing the global setting does not affect projects or scans that do specify their own setting.

Project setting. The Project Settings tab has similar options to enable retention and purge existing unmatched files, except that they only apply to files and scans done under the project. Other than scope, the primary difference from the global retention setting is that the project setting has three possibilities: (1) disabled, (2) enabled, and (3) use the global setting (the default). The global setting only affects scans under a project when option (3) is selected.

Per-scan setting. Each individual signature scan can specify that unmatched files discovered by that scan be retained or not retained; see "Scan Options" below. If no retention option is provided by a scan, retention is determined by the project or global setting as described above.

Note that the determination of whether unmatched files resulting from a scan need to be retained is made at the beginning of a scan and cannot be changed afterwards.

Warning: Once unmatched files are purged, they cannot be recovered except by restoring from backup.

Custom signature matching
When custom signatures are enabled for a project, unmatched files in that project must be retained for the feature to work so that scans of other projects can match against them. In such cases, retention is enabled by default and cannot be disabled unless custom signatures are disabled first.

Note that if a project's custom signature setting is changed from disabled to enabled, unmatched file retention will automatically be enabled as well. However, if retention was previously disabled, unmatched files within that project will be missing, and custom signature matching will not work as expected. In such cases, all versions in that project will need to be rescanned so that all files can be retained.

Scan options
The scan CLI has two new options, --retain-unmatched-files and --discard-unmatched-files, which will retain or discard, respectively, any unmatched files discovered by this scan and this scan only. If either option is supplied, project and global retention settings are ignored; otherwise, retention is determined by project or global settings as described in "Settings". Specifying both options with a single scan is an error.

If scanning with Detect, use one of the following arguments as appropriate:

--detect.blackduck.signature.scanner.arguments='--retain-unmatched-files'

--detect.blackduck.signature.scanner.arguments='--discard-unmatched-files'

Use cases requiring retention
Retention must be manually enabled to support two potential use cases:

Snippet-only scans operating on files previously discovered by a signature scan. If unmatched files from that signature scan were not retained, the subsequent snippet-only scan will be unable to scan them. Note: Snippet-only scans require unmatched file retention to be enabled.

Workflows requiring unmatched files be examined.

Temporary retention
Some signature scan options such as snippet matching, license search, and copyright search will require unmatched files to be retained so that those features can operate. However, if unmatched file retention was not enabled for such a scan, the unmatched files will be purged within a short time after the scan is complete.

Note that these temporarily retained unmatched files may be briefly visible in the source tree view until they are purged.


===== TOPIC: About snippet matching =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id 4cn1yVTydhT1RlDTHpeUdg)

Snippets are small reusable pieces of computer code. A snippet of open source software can easily find its way into your proprietary files. For example, a developer may find a useful function from an open source program and cut and paste that code into their program.

Snippet matching is beneficial to managing legal risk and detecting possible license infringement. A snippet match occurs when a portion of code in your file matches code in one or more KnowledgeBase files.

As the use of open source software is managed through licenses that allow you to use, modify, and/or share the software under defined terms and conditions, it is important to identify the open source software used in your proprietary code so that you can manage the legal risk and detect possible license infringement. Although your proprietary code may include only a portion of open source software code, you still must comply with the license associated with that open source software.

Snippet matching finds these fragments of open source code used in your proprietary files or open source files moved into your proprietary directories and matches that code with open source code found in one or more Black Duck KnowledgeBase files. Though many of the details are proprietary, the mechanism to find snippets is through creating “codeprints” over the contents of scanned source files with a sliding window algorithm. Then, a statistically relevant sampling of those codeprints is sent to the Black Duck KnowledgeBase for matching and the results are presented to the user for review in the Black Duck UI. Codeprints are a type of one-way cryptographic hash which cannot be decomposed back into the original source code. Codeprints are analogous to fingerprints used for crime scene investigation: a fingerprint can be used to identify a person, but a fingerprint cannot be turned into that person. Codeprints allow the Black Duck application to securely and accurately scan code for snippet reuse.

Typically, five to seven lines of average source code can generate a match depending upon the density of non-ignored characters in the line of code. The scanner will ignore white space, tabs, and other non-relevant characters (for example, lines of ******). One line of code can generate a match if it has enough words/characters in it (see certain javascript libraries). Very short lines of code may require more than 20 lines for a match. So, the density of the information content over those lines plays a factor into generating matches. However, other factors can also come into effect and Black Duck has a variety of rules and exclusions to optimize the scanning process and reduce false positives, but which can also impact what gets scanned and what is detected.

Click here for the list of file extensions supported for snippet scanning.

Snippet scanning process
All scanning methods have an option to enable snippet scanning. Enabling the snippet scanning option scans files not identified as open source (proprietary files). The methods to scan your code for snippets are by using:

Signature Scanner command line

Black Duck Detect Desktop

Black Duck Detect

The process for snippet scanning is:

Run component analysis.

The component scan is completed first. This identifies the open source components using directory/file-level signatures.

Generate snippet codeprints.

If enabled, a second-pass snippet scan is performed. This scan analyzes the unmatched files in the initial component scan. For example, individually matched files or files in directories which are matched to open source components do not get scanned for snippets, as they have already been identified and to further scan them for snippets is unnecessary for the typical scanning process. The unmatched files are those which, under the component scan, did not show indications of being open source and have a file extension which indicates they are a source file. These files are the candidates for further analysis.

Note that Black Duck analyzes only the first 1 to 4 MB of data for codeprints. The maximum snippet size can be configured within this range, with the default setting set to 1 MB.

Perform snippet matching.

Snippet codeprints for the file candidates are generated and sent to Black Duck which then sends them to the Black Duck KB Snippet Matching Service. Depending upon the scan parameters selected (see below), Black Duck will send the codeprints for all files or only changed files (delta scans) to the Black Duck KB for matching. The matching service first looks for an exact file match before looking for a snippet match. If any matches are found for the file, a list of matches is produced and a heuristic is run to select the best match as a likely source. Due to the nature of using codeprints over a sliding window, fuzzy matches (inexact or modified textual areas from the original) can be detected. All the matches are then consolidated and available for review in the Black Duck UI.

The user reviews match details.

Unlike components detected via signature or package management scans, components detected via snippet scans are not automatically added to the BOM. This is because the source of a snippet match can often be in many places. Black Duck attempts to choose the best match and show alternative options, but ultimately it is up to the individual users to review these matches and confirm them before they are added to their BOM. While reviewing, a user can look at the matched open source code and (optionally) compare their scanned code with the matched open source code. Please note however, that when viewing the matched area to an open source file, due to the nature of hashed-based scanning using a sliding window algorithm, the highlighted text is only an approximation of the matched area for references purposes. Parts of the match may exceed, and unmatched matched parts may be displayed, in this highlighted area.

Each snippet scanning option is discussed as follows.

Using the Signature Scanner command line
If the Snippets feature is registered on your product registration, you gain access to the following parameters:

--snippet-matching. Using this parameter enables a two-phase approach to scanning. First, a signature scan is completed. Once the signature scan is completed, a snippet scan is performed on unmatched files or files belonging to unmatched directories/archives.

Black Duck recommends using this parameter for snippet scanning.

--snippet-matching-only. When using this parameter, a snippet scan is performed on unmatched files or files belonging to unmatched directories/archives; a signature scan is not executed, but it must already exist. Its purpose is to add a snippet scan to an already existing component scan.

You must have successfully completed a full file scan prior to selecting this parameter, otherwise the scan will error.

Note: Snippet-only scans require unmatched file retention to be enabled.

If you have the Full Snippet Matching registered on your product registration, you gain additional snippet analysis capabilities, allowing for more comprehensive detection of code matches. These parameters become available:

--snippet-matching-all-source. First, a signature scan is completed. Once that scan is completed, a snippet scan is performed for all files with supported extensions (whether they belong to unmatched directories/archives or not).

--full-snippet-scan. Selecting this parameter performs a snippet scan on all applicable files, regardless of if they have changed or not. It effectively overrides the delta scanning capability at the cost of scan performance. On a first time scan, as all snippet candidates are analyzed for matching, this parameter will have no impact.

This parameter must be used with the --snippet-matching or --snippet-matching-only parameter:

With the --snippet-matching parameter: First, a component scan is completed whereby only files that have changed since the previous scan are scanned. Once that scan is completed, a snippet scan is performed on all snippet candidate files.

With the --snippet-matching-only parameter: A snippet scan is performed on all snippet candidate files; a component scan is not completed.

Using this option may cause significant performance and scalability issues, and should only be used in extreme situations.. If you are interested in enabling this feature on your registration key, please contact Black Duck Support for assistance.

Click here for more information on using the command line.

Note: Snippet scanning cannot be completed offline as it requires communication with the Black Duck server.

Using Black Duck Detect Desktop
To enable scanning for snippets, select the select Snippet Scanning from the Settings options and enable it. Selecting this option runs the scanner using the command line --snippet-matching parameter, as described above.

Using Black Duck Detect
Use the --detect.blackduck.signature.scanner.snippet.matching property to enable snippet scanning in Black Duck Detect. With this property enabled, Black Duck Detect uses the command line --snippet-matching parameter, as described above.

Uploading source files for snippet matching
Black Duck provides the ability for you to upload your source files so that BOM reviewers can see the file contents for reviewing snippet matches from within the Black Duck UI. When source files are uploaded, Black Duck provides a side-by-side comparison of the source file to the match which can help BOM reviewers in the evaluation and review of the snippet match.

After your administrator has enabled source uploads, as described in the installation guides, use the Signature Scanner and include the --upload-source parameter when using the --snippet-matching or --snippet-matching-only parameter.

Reviewing snippet matches
It can be difficult to determine where a snippet of code originated; in other words, which open source supplied the snippet of code. The matching process attempts to select the best match for a snippet of code by selecting a component and version in the following order:

Highest KB ranked component/version.

Highest license risk component/version.

Earliest version of component by release date.

Component with the most versions for which a match appears.

As snippet matching is an imprecise technique, snippet matches must be reviewed prior to including these matches in your BOM. Use the Source tab, as described here, to determine if the snippet match is relevant; in other words, does this snippet belong in your BOM? If so, determine if the snippet match is correct.

After reviewing the snippet match, add it to your BOM. The component is shown with:

Match type = Snippet

Usage = Source Code

Any policies you have created execute.

Retaining partial snippet identifications
By default, identifications you made to partial snippet matches are not retained in subsequent snippet rescans.

You can change this default setting so that you can minimize the number of snippet matches you need to re-identify: in the project's Settings tab, in the Snippet Adjustments section, select Apply IDs from partial snippet matches to new exact file matches.

Snippet matches and Vulnerabilities
[HUB-16619, 16621]Black Duck does not include any vulnerabilities related to components/versions that are identified through snippet matching only: vulnerabilities are not counted when showing the total number of vulnerabilities for a project/project version and are also excluded from vulnerability reports. Black Duck will add vulnerabilities/security risk identified by a snippet match if another type match type (for example, exact) identified the same component/version.

Modifying the default maximum snippet file size
By default, Black Duck only analyzes the first 1MB of data for snippet codeprints.

You can modify this default value and select a value from 1MB to 4MB.

To modify the default maximum snippet file size:

Log in to Black Duck with the System Administrator role.

Click .

Select System Settings.

Click Scan in the left-hand menu.

In the Snippet Max File Size section, enter a value from 1 to 4 to set the maximum file size in MB for snippet scanning.

Click Save.


===== TOPIC: Snippet extensions =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id v9G2aOJN~T8F3W8rpKLcQQ)

These are the file types supported for a snippet scan.

Extension
Language

.4th
Forth

.actionscript
ActionScript

.ada
Ada

.adb
Ada

.ads
Ada

.aidl
Interface Definition Language (IDL)

.as
ActionScript

.as8
Assembly

.asm
Assembly

.asp
ASP.NET (C#)

.aspx
ASP.NET (VB)

.aug
Augeas

.awk
Awk

.bas
Classic BASIC

.bash
Shell

.bat
Windows batch

.bf
Brainf*ck

.bfpp
Brainf*ck++

.bi
Structured BASIC

.bms
Text

.bmx
BlitzMax

.boo
Boo

.c
C, C++

.c#
C#

.c++
C++

.cbl
COBOL

.cc
C++

.cfc
ColdFusion

.cfm
ColdFusion

.cgi
Text

.chai
ChaiScript

.clj
Clojure

.cljc
Clojure

.cljs
Clojure

.cls
Visual Basic

.cmd
Rexx

.com
DCL

.cpp
C++

.cpy
Text

.cs
Text

.cu
CUDA

.cuh
CUDA

.cxx
C++

.d
D

.dpk
Delphi

.dylan
Dylan

.e
Eiffel

.ec
eC

.eh
eC

.el
Emacs Lisp

.erl
Erlang

.es
ECMAScript

.exec
Rexx

.exheres-0
Exheres

.exlib
Exheres

.f
Text

.f77
Text

.f90
Text

.factor
Factor

.for
Text

.fpp
Text

.fr
Forth

.frag
OpenGL Shading language (GLSL)

.frm
Visual Basic

.frx
Visual Basic

.fs
F#

.g77
Fortran (free-format)

.g90
Fortran (free-format)

.glsl
Fortran (free-format)

.go
Go

.groovy
Groovy

.gs
Genie

.h
C, C++

.h++
C++

.haml
Ruby

.hh
C++

.hpp
C++

.hrl
Erlang

.hs
Haskell

.hx
Haxe

.hxx
C++

.i
Fortran (fixed-format)

.i3
Modula-3

.idl
Interface Definition Language (IDL)

.inc
Text

.jar
Java archive

.java
Java

.js
JavaScript

.jsp
Java, JavaScript

.jws
Java

.kt
Kotlin

.l
C

.lhs
Haskell

.lisp
Lisp

.lsp
Lisp

.lua
Lua

.m
Text

.m2
Modula-2

.m3
Modula-3

.m4
Text

.ml
OCaml

.mli
OCaml

.mm
Java

.mod
Modula-2

.nb
Mathematica

.nbs
Mathematica

.octave
Octave

.pas
Pascal

.php
PHP

.php3
PHP

.php4
PHP

.php5
PHP

.phps
PHP

.phtml
PHP

.pl
Prolog

.pm
Perl

.pp
Puppet

.py
Python

.r
R

.r3
Rebol

.rb
Ruby

.rc
Text

.reb
Rebol

.rebol
Rebol

.rexx
Rexx

.rs
Rust

.ru
Ruby

.s
Assembly

.sc
Scala

.scala
Scala

.scm
Scheme

.sh
Shell

.sqb
SQL

.sql
SQL

.ss
Scheme

.st
Smalltalk

.swift
Swift

.tcl
Tcl

.tk
Text

.ts
Typescript

.v
Coq

.vb
Visual Basic

.vba
Visual Basic

.vbe
VBScript

.vbs
VBScript

.vert
OpenGL Shading Language (GLSL)

.vhd
VHDL

.vhdl
VHDL

.vim
Vimscript

.y
Text

.z80
Assembly

.zip
ZIP archive


===== TOPIC: About custom scan signatures =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id 9b7OYGYcCEuhsLnkpuAmeg)

Your software projects may contain a mix of open source, third-party, and proprietary software components. While Black Duck KnowledgeBase can identify your open source components, it cannot identify third-party or proprietary software components. As such, your BOM may not include all the software components used in your code.

To ensure that your BOM tracks all your code, you can enable custom scan signatures which you can use to identify third-party and proprietary software used in your code. Once identified, and displayed in your BOM, you can track the use of proprietary code within your organization and ensure that you meet the license obligations required by your third-party software,

Understanding the custom scan signature process
Custom code signatures is an optional feature. Once enabled, the match service uses these signatures to identify where internal components are used in your applications. The internal component would need to be scanned by Black Duck with custom scan signatures enabled with Retain Unmatched File Data enabled.

Unlike Black Duck KnowledgeBase, custom scan signatures reside on your local Black Duck instance (whether the server is on premises or hosted by Black Duck).

Please note, there may be performance issues when using this feature.

Identifying custom code signatures in your code
As the scan client scans the code, it generates “signatures” of the files and directories it is scanning. After the scan completes, these signatures are initially sent to the Black Duck KnowledgeBase (KB) web service where the match service uses the signatures to identify the open source components/versions that are contained in the code being scanned. After identifying the open source components, these signatures are then sent to your local Black Duck instance where the match service compares the signatures to the custom scan signatures. After identifying the custom code signatures that are in the scanned code, the BOM is then created.

By default, custom scan signatures have been limited to the top five levels in the directory structure. System Administrators can modify the global default value. Global Project Administrators and Project Managers can modify the setting for a specific project.

Defining default scanning levels
Users with the system administrator role can define the depth of the scan, as measured by number of levels in the directory structure, from root, to perform custom signature scanning. The default level is 5.

To configure the default custom signature scanning level:

Log in to Black Duck with the System Administrator role.

Click .

Select System Settings.

Select Scan from the lefthand menu.

In the Custom Scan Signature Level section, enter an integer for the number of levels to perform custom signature scanning. You cannot enter 0.

Click Save. To indicate that the default value has changed, the button changes to Saved.

Custom scan signatures on the project level
To enable custom scan signatures for a project:

Select the Settings tab.

Check the Custom Scan Signature checkbox. You can also set the custom scan signature depth.

Click Save.

Creating custom scan signatures
Custom code signatures are managed as projects and after identifying the code the custom code signatures are pulled into the BOM as a subproject.

Note: A project needs to be created before and custom signatures must be enabled for that project before taking advantage of this feature. Also, ensure purging unmatched data is disabled before running a scan.

To create custom scan signatures:

Scan the third-party or proprietary code you wish to identify as a custom scan signature.

Use the --detect.blackduck.signature.scanner.individual.file.matching property set to ALL in Black Duck Detect.

Map the scan to a project version.

Identify this project as a custom scan signature in the project's Settings tab:Enable the feature

Optionally, select the depth, as measured by the number of levels in the directory structure, from root, to perform custom signature scanning. The value shown here is the default value, as defined by your system administrator.

Click Save.

Scan your code. The custom scan signature appears in your BOM as a subproject:

The Source column displays the number of components in the subproject.

Note the following:

If a project contains several versions of a custom scan signature project, the BOM will display only one match to one version of the custom code signature project.

If the custom scan signature project contains open source components, values for security and operational risk may also appear in the BOM.

Although you may have selected only one custom code signature project, if you have scanned several projects, you will experience performance issues.

Policy violations within the subproject will not appear in the BOM. However, a policy violation will appear in the BOM for the subproject if a policy rule is violated at the project level.

Users who do not have permission to the subproject will not be able to drill down to view additional data about that project version.

A Custom Scan Signature filter has been added to the Project dashboard and the BOM page to help you find custom scan signature projects.

Associating custom components to custom scan signatures
Create the custom component.

Users with the Component Manager role can create custom components.

Create a custom scan signature, as described above:Scan the code for the custom component and map the scan(s) to a project version.

In the project's Settings tab, select the option to enable custom scan signatures.

Define the number of levels to scan. The value shown here on the Settings tab

Click Save.

Select to view the project version created in step 2.

From the BOM page, select the Source tab and select the top node.

Modify the match for the custom component: Click Edit to open the Edit Component dialog box.

Select the custom component created previously and click Update.

Click here for more information on using the Source tab.

Disabling custom scan signatures
If you experience significant performance degradation in scanning, you can disable this feature.

To disable custom scan signatures:

Clear the custom scan signature option for all projects.

Rescan your code.


===== TOPIC: Approved signature lists =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id w3UP~N6p~JW9HBed7xlmbg)

As the Signature Scanner examines files, it generates “signatures” of the files and sends SHA-1 and clean SHA-1 signatures to Black Duck's web application. Black Duck filters these signatures based on the individual file matching parameters (if selected) and/or allowed signature lists, which you can create. Black Duck then sends the signatures to the Black Duck KnowledgeBase (KB) web service to identify the open source software contained in the your scanned code.

You can create an allowed signature list for SHA-1 and/or clean SHA-1 file extensions. Each list is optional and works independently of the other list.

To create a list of approved signatures::

Use one or both of the following parameters in the Signature Scanner:--binaryAllowedList x, y, x where x, y, z are the approved file extensions for SHA-1 (binary) files.

--sourceAllowedList a, b, c where a, b, c, are the approved file extensions for clean SHA-1 (source code) files.

Create an environment variable. The following example is for SHA-1 and clean SHA-1 signatures for Linux or Mac OS X.

export JAVA_TOOL_OPTIONS="-Dblackduck.scan.cli.BinaryAllowedList=x,y,z -Dblackduck.scan.cli.SourceAllowedList=a,b,c"
For Windows systems, use the Control Panel to access the Advanced System Settings dialog box to create the environment variable.

If you enable individual file matching (using the--individualFileMatching parameter) in Signature Scannerand create list(s) of allowed signatures, the outcome depends on the option you select:

source optionReplaces the existing file extension for the source option with the list of file extensions from your clean SHA-1 signature list (sourceAllowedList).

Does not use the list of file extensions from your SHA-1 signature list binaryAllowedList .

binary optionReplaces the existing list of file extensions used for the binary option with the list of file extensions from your SHA-1 signature list (binaryAllowedList).

Does not use the list of file extensions from your clean SHA-1 signature list (sourceAllowedList).

all optionMatches with all file extensions.

both optionOnly uses the file extensions from your SHA-1 and clean SHA-1 signature list ( binaryAllowedList  and sourceAllowedList).


===== TOPIC: Understanding component matching in Black Duck SCA =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id TqTYYf4__dniw~C1VDa14g)

Black Duck SCA uses sophisticated matching techniques to identify components in your codebase. As customers increasingly use package manager-produced SBOMs and other scanning methods, understanding how Black Duck identifies and matches components becomes essential. This document explains our fuzzy matching and match correlation capabilities, providing clarity on how components are identified during package manager and SBOM import scans.

Component Identification Process
Black Duck SCA employs a multi-layered approach to component identification:

Exact Matching: First, we attempt to find an exact match for components based on their package URL (PURL) or other identifiers.

Fuzzy Matching: When exact matches aren't found, we employ fuzzy matching techniques to identify similar components.

Match Correlation: For scans using multiple techniques, we use match correlation to consolidate and improve results.

Package URL (PURL) Matching Elements
Package URLs (PURLs) contain several elements that Black Duck uses for matching. Below is a table showing which elements we consider mandatory for accurate matching:

PURL Element
Required for Matching
Notes

Type

Package manager type (npm, maven, etc.)

Namespace

Organization or grouping

Name

Component name

Version

Component version

Architecture

Optional but considered when available

Epoch

Optional but considered when available

Qualifiers

Optional but considered when available

Subpaths

Optional but considered when available

For detailed PURL specifications, refer to the official PURL specification.

Fuzzy Matching Process
When exact matches aren't found during package manager or SBOM import scans, Black Duck employs fuzzy matching through the following process:

Component Name and Version Analysis: We analyze variations of component names and versions.

Namespace Flexibility: We consider potential variations in namespaces.

Version Normalization: Version strings are normalized to account for different versioning formats.

Knowledge Base Comparison: The processed information is compared against our Knowledge Base to find the closest match.

For example, if an exact match for "org.example:library:1.0.0" isn't found, our fuzzy matching might identify "org.example:library:1.0" or "org.example.library:1.0.0" as potential matches.

Match Correlation vs. Fuzzy Matching
It's important to understand the difference between these two techniques:

Fuzzy Matching: Applies to a single scan type, looking for approximate matches when exact matches aren't found.

Match Correlation: Combines results from multiple scan techniques (e.g., signature scan and package manager scan) to provide more accurate identification.

To enable match correlation when using Detect, use the --detect.blackduck.correlated.scanning.enabled=true option.

Architectural Components Involved
The matching process involves several architectural components:

Knowledge Base (KB): Contains the comprehensive component information used for matching.

Match as a Service (MaaS): Handles the complex matching algorithms.

SCA Scan Service (SCASS): Coordinates scanning and initial processing.

Note: Fuzzy matching and match correlation features are not currently supported for air-gapped (KB on-premise) installations.

Ongoing Improvements
Component matching is an area of active development at Black Duck. We continuously refine our algorithms and processes to improve match accuracy. We welcome customer feedback on matching results.

If you have questions about specific fuzzy or correlated matches, please submit a support case through the standard process. Your feedback helps us improve our matching capabilities.


===== TOPIC: Unconfirmed snippets and unmatched components =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id p35Abo8Xh6Jgt~4A~qRPEA)

If there are any unconfirmed snippets, you will see them displayed on the right side of the Risk graphs. Clicking this link will take you to Source view in order to take action on these items.

Note: Unmatched components are found on the Match Review page for the project version.


===== TOPIC: Reviewing snippet matches =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id lUkziTPR60JPYlFv1Hvnwg)

Use the Source tab to determine if the snippet belongs in your BOM and if so, if the snippet match is correct.

Click here for more information on using the Source tab.

Snippets in the BOM
If a snippet scan has been run and snippet matches were found, a snippet badge appears next to the risk charts in the BOM indicating the number of snippets that need confirmation.

By default, the BOM does not display your unconfirmed snippet matches. Unlike reviewing a component in the BOM (which marks all instances of that component as reviewed) snippet matches are confirmed on the match level. Only after a snippet match has been confirmed will it appear unfiltered in the BOM.

Retaining partial snippet identifications
By default, identifications you made to partial snippet matches are not retained in subsequent snippet rescans.

You can change this default setting so that you can minimize the number of snippet matches you need to re-identify: in the project's Settings tab, in the Snippet Adjustments section, select Apply IDs from partial snippet matches to new exact file matches.


===== TOPIC: Match Review =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id WHtkJSD7NH8Cv1boCVUNdA)

The Match Review feature provides a dedicated workspace for reviewing and managing component matches that require additional verification before being included in your project's Bill of Materials (BOM). This feature helps ensure the accuracy of component identification by allowing you to review and confirm matches that have some degree of uncertainty or ambiguity.

What Components Appear in Match Review
Components appear in the Match Review page when they meet specific criteria that indicate potential uncertainty in their identification:

Components with unknown versions (from binary scans)

Components below the match score threshold (configurable globally via component match review settings)

Unmatched components or external IDs from package manager and SBOM import scans

Ignored components from the BOM when the Ignored filter is activated

Important: Components in Match Review are not included in reports or SBOMs until they are reviewed and promoted to the main BOM page.

Accessing Match Review
To access the Match Review page:

Navigate to your project version

Go to the Components section

Select the Match Review tab

Match Review Page Overview
The Match Review page contains the following features; the review categories filters and the match review table.

At the top of the page, you'll find review category filters that display the count of components in each review state: Unknown Version, Low Match Score, Unmatched, and Ignored. Clicking on any category will filter the table to show only components in that specific state, allowing you to focus on particular types of matches that require attention.

Important: Ignored components are not displayed in the Match Review table unless the Ignored filter is activated.

The central match review table displays all components requiring review in a structured format. Each row represents a component with columns showing key information:

Policy Violation: Indicates whether the component has any associated policy violations

Component/ID: Displays the component name and identifier information

Match Type: Indicates the type of match (e.g., exact match, binary, SBOM)

Score: Shows the match score for the component match

License: Displays license information associated with the component

Vulnerabilities: Shows the number of vulnerabilities identified for the component

Operational Risk: Indicates the operational risk level of the component

Actions: Provides an options menu for performing review actions on individual components.

Match Review Sidebar
Selecting a component or ID opens the Match Review sidebar. The Match Review sidebar displays comprehensive details about the selected component, enabling users to make informed decisions regarding matches.

In cases where multiple potential matches exist, the sidebar also shows a list of alternative matches. Each alternative entry includes key identifying information, and users can choose to match the component to any of these alternatives directly from the sidebar. This makes it easier to evaluate available options and quickly correct or refine the match without navigating away from the review workflow.

The panel is organized as follows:

Component/ID: The name and identifier of the component are displayed at the top for quick reference.

Action Buttons: Below the component name, users can take actions on the match with available buttons:

Match: Unmatched components offer additional capabilities for handling internal or proprietary components:

Local Matching (Project Version Specific)

Local match to existing KB/custom component: Affects only this project version

Local match to new custom component: Create a new custom component for this project version only

Global Matching (Requires a user with both the Component Manager and Project Manager roles)

Global match to existing custom component: Future scans with the same external ID will automatically match to this component

Global match to new custom component: Create a new custom component that will be used for future matches across all projects

Confirm: Approve the match and promote it to the BOM.

Edit: Modify the match details if necessary.

Ignore: Mark the match as a false positive.

Unignore: If the component was ignored in the BOM, it can be unignored in Match Review. This returns the component to the BOM. Components that were ignored in Match Review remain there as either ignored or unignored.

Match Type: The type of match is indicated, which may include:

Unknown Version

Low Match Score

Unmatched

Ignored

Vulnerabilities and Licenses: This section displays any associated vulnerabilities and licenses for the component.

Source Information:

Match Score: Displays the score level of the match.

KB Artifacts Matched: Indicates the number of Knowledge Base artifacts matched.

Version Ambiguity: Shows the number of component versions involved.

Match ID: Lists the identifier for the match.

Type: Describes the match type.

File Path: Provides the path related to the match.

Fields Section:

SBOM Fields: Displays any SBOM Fields activated.

Custom Fields: Indicates if there are any custom fields associated with the component.

Comments Section: Users can add and view comments related to the match, facilitating collaboration and discussion.

Details Section:

Component Links: Provides a URL link to more information about the component.

Description: Offers a brief description of the component.

Tags: Lists any relevant tags associated with the component.

Review Actions
When reviewing components, you have several options available:

Confirm Match: Approve the component and promote it to the main BOM/Components page

Edit: Manually change the match to a different component and/or version

SBOM Fields: Access and edit SBOM-specific field information

Comments: Optionally add comments for any review action

Ignore: Mark as a false positive and move to ignored state

Unignore: If the component was ignored in the BOM, it can be unignored in Match Review. This returns the component to the BOM. Components that were ignored in Match Review remain there as either ignored or unignored.

Generate Support Bundle: If you find discrepancies in component identification, licensing, or vulnerability data in your project's Bill of Materials (BOM), you can generate a KnowledgeBase (KB) support bundle directly from here. This bundle automatically gathers all necessary component data for the support team, streamlining the investigation process and reducing the need for additional communication when opening a support case.

Match Review supports bulk operations for efficiency:

Confirm: Approve multiple selected components simultaneously

Comment: Add a comment to multiple selected components simultaneously

Ignore: Mark multiple components as false positives

Unignore: Mark multiple previously ignored components as active again

Generate Support Bundle: If you find discrepancies in component identification, licensing, or vulnerability data in your project's Bill of Materials (BOM), you can generate a KnowledgeBase (KB) support bundle directly from here. This bundle automatically gathers all necessary component data for the support team, streamlining the investigation process and reducing the need for additional communication when opening a support case.

Note: Bulk actions are not supported for unmatched components, except for the ignore action.

Important Considerations
When using the Match Review feature, it's essential to note the following:

Exclusion from Reports: Items listed in the Match Review are not included in the current reports generated by Black Duck SCA. This includes:

Notices Report: Components marked for review will not appear in the Notices File report.

Version Details > Components Report: Components in Match Review are excluded from this report as well.

SBOM Report: Items from Match Review are not reflected in the SBOM report.

Inclusion in Vulnerabilities: Although components in Match Review are excluded from reports, their associated vulnerabilities are included in the project version's Vulnerabilities tab. This means the Vulnerabilities tab may display risks from components that have not yet been confirmed and promoted to the BOM.


===== TOPIC: Black Duck C/CPP Tool =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id zyf1pOUuubusjbQlmkypCw)

C and C++ projects don't have a standard package manager or method for managing dependencies. It is therefore more difficult to create an accurate BOM for these projects. This leaves Software Composition Analysis tools fewer options than with other languages. The primary options which are available in this context are: file system signatures. Black Duck has a variety of old and new signatures which can be used to build a BOM. In order to effectively use signatures, the tool first needs to know which files to take signatures from. In the past SCA tools have pointed a scanner at a build directory, getting signatures from a subset of files within the directory sub-tree. The problem with this approach is that there are many environmental variables, parameters and switches provided to the build tools, which make reference to files outside of the build directory to include as part of the build. Further, there are, commonly, files within the build directory, which are not part of the build and can lead to false positives within the BOM.

The new Black Duck C/CPP tool avoids the pitfalls described above by using a feature of Coverity called Build Capture. Coverity Build Capture, wraps your build, observing all invocations of compilers and linkers and storing the paths of all compiled source code, included header files and linked object files. These files are then matched using a variety of methods described in the section of this document called "The BOM".

This overview is an excerpt from the documentation that can be found in the Black Duck C/CPP Tool Documentation Portal page along with other details on how to use the Blackduck-C-CPP tool.


===== TOPIC: Running an offline component scan using Signature Scanner =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id dyIZSXfLaxFBA_FltIywfA)

If a client does not have access to Black Duck, you can use the command line for Signature Scanner to run an offline scan to identify the open source software (OSS) components contained in an archive or a directory of files. Running an offline scan lets you:

Use the Signature Scanner to run a scan and save the results to a data file.

Upload the data file from a client that does have access to Black Duck to create a BOM.

Note: An error message appears if you exceed the scan size limit, which is 5 GB. Contact Customer Support if you receive this message.

To run an offline component scan:

Be sure that you have a code scanner role.

Using a client that has access to Black Duck, download the Signature Scanner CLI for the platform where the offline scan will occur.

Move the zip file to the client that does not have access to Black Duck and extract the files.

From the client that does not have access to Black Duck, go to the directory where the Signature Scanner is installed and enter the command to run the scan. For example:

Linux/Mac OS X:

./scan.cli.sh --dryRunWriteDir <data_directory> <scan_path>
Windows:

scan.cli.bat --dryRunWriteDir <data_directory> <scan_path>

Move the data directory that contains the JSON file to a client that has access to Black Duck.

From the client that has access to Black Duck, send the scan data to Black Duck using the user interface or the Signature Scanner.

To send the data using the user interface:

Click .

In the Scans page, click +Add and select Scan File.

Use the Upload Scan File dialog box to locate the JSON file, and click Close.

To send the data using the Signature Scanner CLI:

Open a command prompt.

Go to the directory to which the Signature Scanner is installed and run the following command: For example:

Linux/Mac OS X:

./scan.cli.sh --dryRunReadFile <data directory> --username <username> --host <host> --port <port>
Windows:

scan.cli.bat --dryRunReadFile <data directory> --username <username> --host <host> --port <port>
