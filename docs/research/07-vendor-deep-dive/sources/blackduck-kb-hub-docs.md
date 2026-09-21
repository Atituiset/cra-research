# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q
# Reader base: https://docs.blackduck.com/bundle/blackduck-hub/page/
# Captured: 2026-09-21



===== TOPIC: Hosted vs Air-gapped KnowledgeBase =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id edBsJR9UWygSw1XaZglIuQ)

Notice: This is a non-exhaustive list and any feature not explicitly listed may not be available for air-gapped KnowledgeBase installations.

Core features & scanning techniques

Feature
Included in Hosted
Included in Air-gapped
Notes

Policies

The Policy Management feature enables you to create rules to govern your use of open source components. With policy rules, open source usage can be managed on an exception basis – as long as open source components meet the policy requirements their usage is allowed. Any open source components/versions that fail to meet your policy rules are flagged, enabling you to review and determine if the use of the component should be allowed in the particular application.

Signature scanning

Signature scanning scans an arbitrary file system directory or archive and matches to known components in the Black Duck KnowledgeBase. The core concept behind component scanning and discovery is the ability to compare the signatures of artifacts in the repository with the signatures of all OSS components in the Black Duck KB and quickly recognize a match.

Package manager scanning

Uses the project's package manager to derive the hierarchy of dependencies known to that package manager.

Snippet scanning

Snippet matching is beneficial to managing legal risk and detecting possible license infringement. A snippet match occurs when a portion of code in your file matches code in one or more KnowledgeBase files.

Binary scanning

Binary scanning identifies the open-source security, compliance, and quality risks in the software libraries, executables, and vendor-supplied binaries in use within your codebase.

Black Duck Secure Container scans

When scanning a container using this feature, Black Duck creates a new type of project that manages a new container scan. The container project displays the aggregated BOM and risk, but it also provides a way to view risk layer by layer, specifically adding support for components that are added or removed on a layer.

Vulnerabilities

Vulnerability information, triaging and management features are available in Black Duck.

Real time updates

Update of the hosted KB is done in real-time so new vulnerabilities or components appears continuously. With an air-gapped KB, new vulnerabilities and components only appear when the KB update is performed.

License text and copyright text

Feature
Included in Hosted
Included in Air-gapped
Notes

Template license text

Each license comes with a template version of the license.

Local license text scan

The license search feature to search for license text in your projects. This helps with the reconstruction of the specific custom license text which might be contained in the project source files. See License Detection for more information.

Local copyright text scan

By enabling detection of copyright data when scanning code, users focused on license compliance can reduce license compliance risks by detecting and managing open source software and proprietary copyrights statements.

With this feature, Black Duck performs a search for copyright string text and displays the text found in the Source tab. See Copyright Detection for more information.

Actual license text

Black Duck KnowledgeBase provides the actual license text contained in each version of every component. No big data is shipped with air-gapped KnowledgeBase.

Full copyrights

Black Duck manages copyright statements by the origin name/ID for a component version. Using this feature makes it easier for you to include the full list of copyright holders for the open source components you use in your notices file report. No big data is shipped with air-gapped KnowledgeBase.

Deep License data

Black Duck displays declared licenses for the components in your BOM. However, deep licenses (also known as sub-licenses or embedded licenses) may also exist in your open source components. Deep license data is not enabled by default. No big data is shipped with air-gapped KnowledgeBase.

Cloud scanning services & specific match features

Feature
Included in Hosted
Included in Air-gapped
Notes

SCA Scan Service

Coming in 2026
SCA Scan Service (SCASS) is a scalable solution for performing software composition analysis scans outside of the traditional Black Duck SCA environment. SCASS supports Package Manager and Signature Scans, making it a versatile choice for various scanning needs.

Match as a Service (MaaS)

Match as a Service (MaaS) is a cloud service that identifies OSS components, using data gathered by Component Scanning. MaaS moves the matching logic from the Black Duck server to the KB server for efficiency.

Scan correlation

Correlated Scanning is a scanning method which allows different matching technologies to scan the same application target and correlate results together to perform more accurate component and component version matching.

AI Model Scanning

AI Model Scanning enables organizations to maintain visibility into the AI models they use, monitor associated risks, and ensure compliance with relevant policies.

External integrations

Feature
Included in Hosted
Included in Air-gapped
Notes

SCM Onboarding

SCM repository auto-scanning allows Black Duck to check daily for any changes such as commits, pushes, or merges in the repository branch mapped to your SCM projects and perform scans if changes were made.

Artifactory Integration

BD SCA can be integrated with Artifactory to scan the assets for OSS. Artifactory Integration automatically blocks downloads from scanned Artifactory Repositories that have a Black Duck Policy Violation.

Other features

Feature
Included in Hosted
Included in Air-gapped
Notes

Stateless signature scanning

Stateless Scan is a scan mode that does not create or use any permanent storage within Black Duck, thus there is no bill of material (BOM) stored. It is used to quickly find policy violations within the designated scan target.

Auto BOM re-computation (components)

When the KnowledgeBase (KB) is updated, Black Duck automatically refreshes vulnerability and component information. For air-gapped KB deployments, this refresh is not automatic—projects must be re-scanned or scans manually unmapped and remapped after KB updates to trigger a data refresh.


===== TOPIC: KnowledgeBase service =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id Sh6X2mlHEcNT3WIH7Dp1pA)

Via web services, the Black Duck KB provides the Black Duck application with the most up-to-date information about open-source software without requiring regular updates on your Black Duck server. New vulnerability data is added to the KB hourly; new searchable open-source components are added daily; and new signatures for matching are added 2-3 times per week. Other big data services are updated quarterly.

The signatures of your scanned code are used to match signatures of the open-source software in the KB to identify the open-source software contained in your code. These signatures consist of one-way, encrypted MD5 or SHA1 hashes of file system meta-data and file content. The use of MD5/SHA-1 is purely for signature hashing and is not used for any cryptographic purpose. These signatures (collections and hashes) are sent by the Black Duck application to the KB service. No source or binary code is ever sent off premises. The signatures are formatted as a JSON document and transmitted over HTTPS connections. The scan document can send file paths, file sizes, and some SHA-1 or clean SHA-1 signatures to the Black Duck server. Black Duck does post-processing on this data to create additional proprietary signatures.

Again, customer data sent to increase the accuracy of matching services is not persisted in the KB. It is used during the BOM matching process and deleted afterwards. For those reasons, no logs are produced during this process.

Additionally, the separation of customer data is enforced by the design of the architecture.

Note: The KBMATCH_SENDPATH parameter has been deprecated as of 2023.4.0 and will be removed in a future update. Black Duck users with Match as a Service (MaaS) enabled will not be able to use this parameter. Customers wanting to continue using this option will need to contact Black Duck support to have MaaS disabled for their Black Duck registration keys.

The matching service is described in more detail below.

Match service overview

The client POSTs a JSON document representing a tree structure of scanned nodes, with a set of signatures per node to the match endpoint. The endpoint determines if there are any matches to those signatures. If there are, it returns a JSON document with the same nodes that were sent to the match service, and adds to the document the matches from the KB for each node.

URL format

https://<server>/kbmatch/api/v1/matches/<end-point>?authToken=< >

Header

X-BDS-AuthToken:<>

Request body data

Response

As can be seen from the example above, matching open-source components are returned to the Black Duck application using GUIDs. These GUIDs are then used to retrieve metadata on each of the open-source components using KB services for vulnerabilities, licenses, and other information.

KnowledgeBase feedback service

In the same way that signatures and hashes are sent up to the match service, occasionally these same pieces of information will be sent associated with a specific component and version. This is done in cases where users have corrected (“adjusted”) an identification. This “vote” is recorded absent any customer context whatsoever and is used simply to increase the accuracy of the matching capability. It is in our customers' best interest to share this data as it helps improve the overall quality for the KB. However, if it is desired to not share this data, please refer to the section “Disabling the Black Duck KnowledgeBase feedback service” in the Black Duck installation guide.


===== TOPIC: Understanding the Knowledge Base Update Job =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id vg5CS7xAhhU9lfx_rzkv~w)

An overview of the Knowledge Base update job in Black Duck SCA, explaining how vulnerability data is propagated, notifications are generated, and the limitations users should be aware of.

The Knowledge Base (KB) update job plays a crucial role in maintaining the accuracy and currency of vulnerability information within the system. Its primary functions include propagating newly published vulnerabilities, such as CVEs (Common Vulnerabilities and Exposures) and BDSAs (Black Duck Security Advisories), to Active project versions without requiring a rescan, provided that the Bill of Materials (BOM) remains unchanged.

Key Functions of the KB Update Job:

Propagation of Vulnerabilities: Newly added or deleted vulnerabilities are automatically reflected in the project BOMs.

Notifications and Audit Logs: Notifications are generated for newly added or deleted vulnerabilities, ensuring users are informed of important changes. Audit log entries are created to maintain a record of these updates.

Interaction with Active and LTS Projects: The Knowledge Base (KB) update job plays a critical role in the functioning of both Active and LTS project versions.

Limitations:

The KB update job does not generate notifications for score-only updates or severity changes; these updates are applied silently.

In cases where vulnerabilities transition between identifiers (e.g., from BDSA to CVE), they are treated as new entries, which can reset remediation statuses and comments.

The propagation of vulnerabilities may not be immediately observable if the KB update job has not yet processed a specific project version, or if the job fails or becomes stuck.

Understanding the behavior of the KB update job is critical for effectively managing vulnerabilities and ensuring that your projects are always up-to-date with the latest security information.

What's Coming Next
We are continuously improving the KB update experience. Key areas of investment include:

LTS notification support — enabling notifications and alert integrations for LTS project versions.

Improved remediation continuity — preserving remediation status across vulnerability identifier transitions.

Next-generation notification system — a more flexible and reliable notification framework that will support additional change types.

For the latest on these and other improvements, visit the Black Duck Ideas Portal or speak with your Black Duck account team.


===== TOPIC: Knowledge Base Updates & Vulnerability Propagation =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id 9GjzIEdXVCGbBQcHnvjWnA)

Black Duck SCA automatically keeps your project vulnerability data current through Knowledge Base (KB) update jobs — background processes that continuously propagate newly published vulnerabilities, score changes, and component metadata into your project versions. This page explains how these updates work, what to expect from notifications and audit logging, and how to get the most out of Active and LTS project versions.

Automatic Vulnerability Propagation
When new vulnerability data is published in the Black Duck Knowledge Base, background jobs automatically propagate that data into Active project versions. This means:

New CVEs and BDSAs are applied to all relevant Active project BOMs automatically.

No rescan is required — the system matches new vulnerability data against the existing BOM.

Processing is asynchronous; the time to full propagation depends on the volume of project versions and the health of the job runner.

Component Data Quality Updates
Occasionally, the Knowledge Base team makes structural improvements to component data to ensure accuracy:

Component migrations improve the accuracy of component metadata and matching.

Component deprecations remove invalid or fraudulent components (e.g. fake open-source packages identified on software forges).

Component merges and splits consolidate or separate component records for better data quality.

These changes are applied automatically and may update BOM entries in both Active and LTS project versions to reflect the corrected component data.

Notifications & Audit Logging
Black Duck SCA generates notifications and audit log entries for key vulnerability changes. The following table summarises current notification behaviour:

Change Type

Notification Generated

Audit Log Entry

New vulnerability added to a component
Yes 
Yes 

Vulnerability removed from a component
Yes 
Yes 

CVE ↔ BDSA mapping update
Yes 
Yes 

CVSS / severity score change
—
—

Metadata-only update (description, references)
—
—

Score and metadata changes are applied to your project data but do not currently generate notifications or audit log entries. This is an intentional design decision to minimise notification noise while a next-generation notification system is under development. We plan to revisit score-change notifications as part of that work.

Tip: To verify the most current vulnerability data at any time, refer to the dedicated BDSA or CVE detail page in Black Duck SCA — this always reflects the latest information from the Knowledge Base.

Understanding Remediation Status
When you review and remediate vulnerabilities in your project, Black Duck retains your remediation status and comments. However, there are specific scenarios where a vulnerability may appear as "new" and remediation status is reset:

Identifier transitions: When a vulnerability transitions between a BDSA and CVE identifier (or vice versa), the system creates a new record. Your previous remediation data is preserved in the system but is associated with the original identifier.

Component migrations: If a component is migrated to a new record in the Knowledge Base, vulnerabilities on the updated component are treated as new entries.

We are actively working on improvements to preserve remediation context across identifier transitions — this is a priority item on our product roadmap.

Resolving Data Discrepancies Across Views
Different views in Black Duck refresh at different intervals. If you notice temporary inconsistencies between views:

The BDSA/CVE detail page is always the authoritative source — it reflects the most current Knowledge Base data.

BOM vulnerability pages, dashboards, and reports may take slightly longer to update.

The "Where used" view on a component version can help confirm which projects are affected when the "Affected projects" view has not yet fully refreshed.

These timing differences are expected and typically resolve within a short period as background processing completes.

Best Practices
Check the BDSA/CVE detail page when you need the most up-to-date vulnerability information.

Re-scan a project version if you suspect KB update data has not yet propagated — this forces a full refresh against the latest Knowledge Base.


===== TOPIC: Knowledge Base Interaction with Active and LTS Project Versions =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id KaeGqexq2eesBbNAQa4viQ)

Black Duck offers two project version types, each optimized for different stages of your software lifecycle.

Understanding the KB Update Job Interaction
The Knowledge Base (KB) update job plays a critical role in the functioning of both Active and LTS project versions. In Active projects, the KB update job automatically propagates newly published vulnerabilities, ensuring that your project reflects the most current security landscape. For LTS projects, the centralized architecture allows for efficient updates across multiple versions, enhancing the reliability of vulnerability propagation. Understanding how the KB update job interacts with these project types is essential for maintaining effective vulnerability management and ensuring that your software remains secure.

Active Project Versions
Active project versions are designed for software under active development and provide the fullest set of capabilities, including:

Automatic Vulnerability Propagation: Newly published vulnerabilities from the Knowledge Base are automatically propagated to ensure your project is up to date.

Notifications and Alert Integrations: Receive timely notifications about vulnerability changes and alerts related to your project.

Audit Log Entries: All changes to vulnerabilities are recorded in the audit log for transparency and tracking.

Full Remediation Workflow Support: Comprehensive support for managing and resolving vulnerabilities.

For best results, we recommend keeping project structures straightforward and re-scanning periodically to ensure your BOM reflects the latest state of your codebase.

LTS (Long-Term Support) Project Versions
LTS project versions are purpose-built for released software artifacts where ongoing monitoring is needed, but re-scanning is not expected. Key features include:

Automatic Vulnerability Propagation: Vulnerabilities are propagated using an enhanced, more resilient architecture, ensuring reliability.

Efficient Scalability: Designed to scale efficiently to accommodate large numbers of project versions.

Full Remediation Workflow Support: Complete support for managing vulnerabilities within LTS versions.

Notification and Alert Support: Coming soon; this is our top priority for expanding LTS capabilities.

LTS versions utilize a centralized component catalog, meaning component data is stored once and shared across all projects that reference it. This architecture enables faster and more reliable KB updates at scale.

Which Should I Use?

Scenario
Recommended Type

Software under active development with CI/CD integration
Active

Released products requiring ongoing vulnerability monitoring
LTS

Large-scale environments with many monitored versions
LTS

Best Practices
Use Active project versions for development branches where you need real-time notifications and alert integrations.

Use LTS project versions for released software that requires long-term vulnerability monitoring without re-scanning.

Keep project structures simple — avoid deeply nested sub-project hierarchies for the most reliable update processing.


===== TOPIC: About Black Duck KnowledgeBase components =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id NNskrgBm8NLm_V6Z32hK1Q)

The Black Duck® KnowledgeBase™ (Black Duck KB) is the industry’s most comprehensive database of open source component information. Since 2003, Black Duck has searched the Internet for information on open source software (OSS) components and downloadable source code. The complete version of Black Duck KB includes more than 9 million unique components from more than 50,000 sites and contains detailed data on more than 260,000 actively traced vulnerabilities across billions of lines of code. The Black Duck KB includes detailed data for more than 2,900 unique licenses, including the full license text and dozens of encoded attributes and obligations for each license. Black Duck connects to a version of Black Duck KB hosted in the cloud.

New OSS component versions and meta data, such as vulnerabilities, are continually added and updated to the version of Black Duck KB that supports Black Duck SCA.

The Black Duck KB provides information about OSS components at the component level and at the component version level.

So that your BOM accurately reflects your project, users with the Component Manager role can:

ModifyBlack Duck KB components and/or Black Duck KB component versions.

Undo these modifications and reset the KB data back to its original values.

Define an approval status for a Black Duck KB component and/or component version to ensure that only approved components/version are included in your BOM.


===== TOPIC: Understanding the component information available from the Black Duck KB =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id CBka8gaNq6pk5PNOLl8prQ)

The Black Duck KBComponent Name page displays information about the open source software (OSS) component.

This page is comprised of two tabs: an Overview tab and a Settings tab.

About the Overview tab

The Overview tab displays information such as a status, description, component links, and tags, and information about each of the component versions that are available in Black Duck KB.

A graph at the top of the page shows a history of high, medium, and low vulnerabilities for each version of this component. Use this graph to quickly view vulnerability information for component versions.

Select Previous or Next to view older or newer versions.

Hover over a data point in the graph to view the version, release date, and number of vulnerabilities for this version:

To view information on versions that interest you, use the filter, located above the table, to filter the versions shown in the vulnerability graph and in the table below.

The following information is available for each version:

Column
Description

Version
Release number of this version of the component.

Select the version number to display the Component Name > Version page.

Used Count
Number of project version BOMs in which this version of the OSS project is used.

Tip: Select the number to go to the Overview tab for this version of the OSS component. That tab lists each project and project version in which this version of the OSS component is used.

License
Declared license of this version of the OSS component. Other license types include:

"Unknown" indicates that the OSS component version's license is not known.

"License Not Found" indicates that although researched by Black Duck, no declared license was found for the component.

"No License" indicates that Black Duck has found a declaration of 'No License' for the component.

For known licenses, select the license name to view license details and license text.

Released
The date this version of the OSS component was released.

Security Risk
A graph which shows the number of high risk, medium risk, low risk, and unknown vulnerabilities associated with this version of the OSS component.

About the Settings tab

The Settings tab shows details on this component. Information shown here appears on the Overview tab.

Users with the Component Manager role can use the Settings tab to edit the description, URL, notes, and status for this KB component. Click here for information on editing component information and here for information on modifying a component's status.

Users with the System Administrator role can use the Settings tab to edit the component custom field information. as shown in the Additional Fields section.


===== TOPIC: About the KnowledgeBase Feedback Service =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id Ct~yYWTkhNKuyzDKFUXJ5w)

The KnowledgeBase Feedback Service allows users to submit feedback on component and vulnerability data in Black Duck, helping to improve the accuracy of the Black Duck KnowledgeBase (KB). Feedback is sent when specific adjustments are made to components or matches identified by the KB.

When feedback is sent:

Component adjustments: Feedback is submitted when the component itself is adjusted or when a component's license is modified. Other component adjustments do not trigger feedback submission. Other component adjustments do not trigger feedback submission.

File adjustments: Feedback is sent only when the component matched to a specific file is changed.

BOM adjustments: Feedback is also triggered when making adjustments to a component, version, origin, origin ID, or license for a match made by the KB.

Unmatched files: If you manually identify an unmatched file to a component, feedback is sent. However, feedback is not sent for manually added components that do not have associated files.

Note: No customer-identifiable information is transmitted to the KB.


===== TOPIC: Searching the Black Duck KnowledgeBase =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id a3bEFa4o~zZWCS3tcgqYGw)

You can search for component versions used in your BOMs and/or components in the Black Duck KnowledgeBase (KB).

To search for components :

Click  to open the Find page.

Select the Black Duck KnowledgeBase tab. Note that using the Black Duck KnowledgeBase tab to search for components will not display any custom components used in your projects. Use the Components tab to include these in your search results.

Type your search term in the Search field and/or optionally, select any filters to refine your search.

Optionally, for component searches, save this search, so that the results appear on the Dashboard page.

The Find page displays the components that meet your search criteria.

You can also type your search term in the Search field located at the top of the application and press Enter or click . The Find page appears displaying the search results. Note that entering a global search term initiates a new search and resets any filters you previously selected. Select the Components or Black Duck KnowledgeBase tab and filters to refine the results, as described below.

KnowledgeBase filters
Use the following filters to narrow your results when searching Black Duck KnowledgeBase:

Primary Language. Primary language in which the component is written. The filter displays the list of available languages in descending order of frequency of use in components.

Tags. Available for all components that have tags applied to them to provide additional metadata about the component.

Commit Activity. Represents the trending commit activity level for the open source component over time.

Important: Primary Language and Tags are dynamic search filters. Enter one or more characters in the filter field to retrieve matching values. These filters do not pre-populate with all available languages or tags. Primary language, tags, and commit activity information is provided by Black Duck Open Hub.

Black Duck KB component search results
The following information is shown for each KnowledgeBase component that meets your search criteria:

Select the component name to open the Black Duck KB Component Name page.

View the number of project versions that use this component as shown by the value next to Used By.

Select Project Versions to open the Where Used dialog box.

This dialog box lists the projects that use a version of this component.

Column
Description

Project
Name of the project and version that uses this component. Select the project name to display the project version's Components tab.

Phase
Project Phase.

Component Version
Version of this component used in this project version.

Security Risk

Lists the vulnerabilities for each severity level, from left to right: Critical, High, Medium, and Low.

Select a value to display the Vulnerabilities tab of Black Duck KBComponent Name Version page, which lists the vulnerabilities associated with this version of the component.

For each component, the search results show:Commit Activity.

Last commit date.

Total number of versions for this component.

Select Tags to view the tags for this component.

The URL in the upper right corner is the URL for this component.

Exporting to CSV
You can export your search results to CSV which converts the individual rows to tabular data. To do so, click the  button and select CSV.


===== TOPIC: Black Duck Security Advisories =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id yZke~Uck5bOf4XmEKjiXSQ)

Black Duck Security Advisories (BDSAs) are a proprietary vulnerability data feed curated by the Black Duck Cybersecurity Research Center (CyRC). They provide more comprehensive coverage of vulnerabilities compared to the National Vulnerability Database (NVD), offering timely insights on severity, impact, and exploitability.

BDSAs include actionable remediation guidance, detailing fixed versions, patches, known exploits, and workarounds. Additional validated references can be found under the Technical page of each BDSA record.

The CyRC team conducts thorough research, cross-checking vulnerabilities against affected component versions for accuracy. If a BDSA is not linked to a CVE record, it means further research has determined that the component is not impacted by the vulnerability. BDSAs are updated frequently, often on an hourly basis, to reflect new vulnerabilities.

In contrast to BDSAs, NVD CVE records are not typically cross-validated and may update more slowly. Users should view BDSA records as complementary insights that enhance understanding and decision-making regarding open source security vulnerabilities.

Viewing a BDSA record
To view a BDSA record:

Use the Search feature to locate BDSAs.

For example, search for BDSA-2017 to see the list of Black Duck Security Advisories from 2017.

Select a BDSA to view the record.

Use the Vulnerabilities tab for a project version to view the vulnerabilities for a project version BOM.

Vulnerabilities with identifiers beginning with BDSA are proprietary findings curated by the Black Duck Security Advisory (BDSA) team.

Click  next to the vulnerability to reveal additional details. Then click the View BDSA record link to open the full BDSA record.

Tip: Use your browser print feature to print the information shown in a tab.

Overview tab
By default, the Overview tab appears and displays the following information:

The header bar displays the following information:

BDSA ID: The unique identifier assigned to the BDSA, which serves as a reference for the specific vulnerability.

Related Records: This section lists links to associated Common Vulnerabilities and Exposures (CVE) and European Union Vulnerability Database (EUVD) records, offering users additional context and remediation options related to the same vulnerability or component.

Published: The date when the National Vulnerability Database (NVD) published the CVE. This indicates when the vulnerability was officially recognized and made public.

Updated: The last modified date by the NVD, reflecting when the CVE record was last updated with new information or corrections.

Under Review: Some BDSAs display the status "This vulnerability is currently under review with Black Duck." Reviews are carried out on a cyclic basis for a defined period — sometimes up to a year — depending on the nature of the vulnerability and whether further information may become available. For example, embargoed vulnerabilities may have no technical information available for six to nine months after initial disclosure. Once all relevant information has been gathered, analyzed, and included in the BDSA, the Under Review status is removed. The review process is essential for ensuring scoring accuracy, as the publication of exploit code can impact temporal metrics and the overall severity rating. The Updated date always reflects the most recent changes to the record.

The Overall Score graphic provides the following information: represents the

Shown here are the:

Common Vulnerability Scoring System (CVSS): Score for the BDSA.

Exploit: If a known exploit exists, this link provides a technical description of the vulnerability, detailing how it can be exploited. It includes examples illustrating how a specially crafted message can lead to arbitrary content injection into the HTTP response, highlighting the conditions necessary for a successful attack. If there is no known exploit, the label will simply state "No Known Exploit," indicating that there are currently no publicly available methods to exploit this vulnerability.

Solution: This link offers guidance on remediating the vulnerability. It includes references to relevant advisories, vendor upgrades, and patches, along with a proof-of-concept example that illustrates how the vulnerability operates. If there is no known solution, the label will state "No Known Solution," indicating that no remediation steps are currently available.

The Description section provides a detailed overview of the vulnerability associated with the BDSA. It includes information on the nature of the vulnerability, its potential impact on affected systems, and the conditions under which it can be exploited. The description may also outline the software or components affected, attack vectors, and any known mitigations or recommendations for addressing the vulnerability. This information is crucial for users to understand the context and significance of the CVE, facilitating informed decision-making regarding remediation strategies.

The Vulnerability Tags section highlights specific attributes or classifications associated with the vulnerability record, providing context and important details to help users understand the nature and implications of the vulnerability. Each tag may include a Solution section, which outlines available fixes, patches, and references to relevant commits and versions.

Zero-click Remote Code Execution (RCE). This vulnerability can result in the execution of code on the system, triggered by a remote attacker without requiring or relying on any third party action.

Malicious Code Identified. This software contains code with malicious intent and is designed to have harmful or destructive consequences if executed within your system.

Embargoed Vulnerability Details. Technical details of this vulnerability are currently under embargo and the details are not published by the vendor at this time. An embargo remains in place for a fixed period. The BDSA record will be reviewed and updated with further details where possible once the embargo has been lifted.

Unconfirmed Vulnerability. This vulnerability does not have a code-based fix because the vendor has decided that the behavior of the component is intended and does not believe there is a vulnerability. The vendor may have resolved this issue by providing clarification in their documentation.

Automated Security Advisory (ASA). Automated Security Advisories are automatically created by Black Duck's Cyber Security Research Center using automated AI tools. ASAs are created from various trusted security feeds such as the GitHub Security Advisories (GHSA) feeds along with automated vetting using AI tooling. These advisories are designed to supplement the BDSAs identified and verified by our Cyber Security Research Center.

CISA Known Exploited Vulnerability. This vulnerability is listed in the Cybersecurity & Infrastructure Secrity Agency's (CISA) catalog. All federal civilian executive branch agencies are required to remediate vulnerabilities in the KEV catalog within prescribed timeframes. Please visit CISA's Known Exploited Vulnerability Catalog page for more information.

AI Assisted. AI Assisted Security Advisories are automatically created by the Black Duck Cybersecurity Research Center using automated AI tools. These BDSAs have not been independently verified by the BDSA team but are created using automated processes and generative AI assistance. These advisories are designed to supplement the BDSAs identified and verified by the Cybersecurity Research Center.

Note: This tag has been deprecated and will no longer be included in new BDSA vulnerabilities.

Potential Remote Code Execution. This vulnerability has the potential to cause a remote code execution vulnerability however this has not been proven in the wild or via a known exploit.

Remote Code Execution Requiring User Input. This vulnerability can lead to a remote code execution vulnerability however it requires specific user input to be provided.

Rapid Review. BDSA Rapid Review vulnerabilities are produced en masse to expand our BDSA coverage for lower popularity components. These BDSAs are created with AI and automation assistance, including generating the text description. These have not been researched independently by our Vulnerability Analysis team but have been verified for affected component version ranges. These BDSAs enable proactive vulnerability notification for an expanded coverage of less popular OSS components using highly scalable technology.

The Scores and Metrics section displays the scores for the related BDSA and NVD records (if applicable), based on the Common Vulnerability Scoring System (CVSS). Select a value above the graph to view the information in the graph and details below.

This section may also display a comparative, side-by-side graph if the vulnerability also has a NVD record.

Note: For more information on vulnerability metrics, visit the NVD web site: https://nvd.nist.gov/vuln-metrics

Affected Projects tab
Select this tab to see a list of your projects that are affected by this vulnerability.

This tab lists all projects affected by this vulnerability:

Project name and version affected by this vulnerability.

Component name and version that contains this vulnerability.

Component origin that contains this vulnerability.

Remediation status of this vulnerability. Possible values are: New, Needs review, Mitigated, Patched, Duplicate, Remediation Required, Remediation Complete, or Ignored.

Target date for remediating this vulnerability.

Actual date this vulnerability was remediated.

Select  in the row of a project and select:

View all vulnerabilities to view all vulnerabilities affecting this project version.

View related files to view to display the Source tab filtered to display the affected files.

Use this tab to remediate the vulnerability for one or more projects by origin:

In the row of the single project you want to remediate, do one of the following:Select , select Update Remediation Plan, enter the remediation details, and click Update.

Select  and click Remediate. Enter the remediation details, and click Update.

For multiple projects that need the same remediation status, select  in each row and click Remediate. In the Bulk Remediation dialog box, enter the remediation details, and click Update

Technical tab
Select the Technical tab to view a technical description and a list of references and related links.

Included in the References and Related Links section is a list of Key Events:

Discovered. Date that the vulnerability was discovered.

Vendor Notified. Date the official vendor was notified of this vulnerability.

Vendor Fix. Date that the official vendor released a patch or upgrade to fix this vulnerability.

Disclosure. Date the vulnerability was first publicly disclosed, whether as a bug or as a security vulnerability.

Vulnerability Age. Today's date - Disclosure date.

Exploit Available. Date an exploit became publicly available for this vulnerability.

Components tab
Select the Components tab to view a list of all known component versions affected by this particular BDSA vulnerability record.

CVE References tab
Select the CVE References tab to view links for additional information.

Settings tab
Use this tab to manage the global remediation for this vulnerability. Click here for more information.
