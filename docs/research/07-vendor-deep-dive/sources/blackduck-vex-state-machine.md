# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q
# Reader base: https://docs.blackduck.com/bundle/blackduck-hub/page/
# Captured: 2026-09-21



===== TOPIC: Vulnerability Exploitability EXchange (VEX) =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id hjDYPOYyMLO5CnhaO7wqrA)

Creating a Project Version VEX Report
Project Version VEX reports focus on vulnerabilities specific to individual project versions, enabling targeted remediation strategies. Use the steps below to generate a VEX report for a specific project version:

Select the desired project name using the Watching or My Projects dashboard.

Select the version of the project for which you want to run the report.

Select the Reports tab.

Select + Create Vulnerability Report → Vulnerability Exploitability EXchange (VEX): CSAF 2.0.

Select a Template.

Optionally, you can expand the Template Details section to see which options are enabled in the selected template.

Select Create to generate the report.

The following links appear when the report completes:

csaf-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report.

Select the link to view the report.


===== TOPIC: Remediating security vulnerabilities =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id kPr4yvC2pKpFQ4MhllXwHg)

Vulnerabilities have a remediation status assigned to them. A new vulnerability can have a status of New, Needs Review, Patched, or Duplicate.

The following table describes each remediation status and whether a vulnerability with this status is included in the security risk calculations:

Remediation Status
Included in Security Risk Calculation?
Definition

Duplicate
No
This vulnerability is a duplicate.

Ignored
No
The vulnerability has been ignored.

Known Affected

Yes
Actions are recommended to remediate or address this vulnerability.

Known Not Affected

No
A justification must be provided to ensure that the decision is properly documented.

Mitigated
No
The vulnerability has been mitigated.

New
Yes
Black Duck has determined that a vulnerability affects this component version.

Needs Review

Yes
Black Duck cannot determine if a vulnerability definitely affects this component version. This can occur when a component version is known to contain a vulnerability, but it cannot be determined whether the patch or sub-version being used is affected by this vulnerability.

Patched
No
The vulnerability in this version of a Linux distribution package has been patched. Although a vulnerability has been reported on the overall component version, the vulnerability does not affect this specific matched version as the version has been patched from the source from where it came.

Remediation Required
Yes
Remediation is required for the component version.

Remediation Complete
No
Remediation for the vulnerability is complete.

Under Investigation
Yes
It is not yet known if the product versions are affected by the vulnerability, but an update will be provided in a later release.

Remediating a vulnerability
You may wish to change the remediation status after reviewing the severity of the vulnerability. Black Duck can help you determine which version you should use when a component has a vulnerability. Black Duck helps you to understand your options when a component has a security vulnerability.

Important: If a CVE record has a related BDSA record (or vice versa), it cannot be remediated unless that vulnerability record type is prioritized in the Security Risk Ranking. This is due to the fact that the non-prioritized vulnerability record is not being used as a determinant and is not used to calculate security risk.

Note: You can select any value for the remediation status. Selecting Remediation Complete, Mitigated, Patched, Known Not Affected, or Ignored removes the vulnerability from the security risk calculations.

You can remediate a vulnerability for current projects or set a global remediation status that applies to new instances of that vulnerability when that component appears on new BOMs.

Only users with the appropriate role can remediate vulnerabilities.

To remediate vulnerabilities for current projects:

Use this method to identify and remediate the vulnerabilities affecting a specific project version.

Select the version name to open the Components tab and view the BOM.

Select the Vulnerability tab which lists all vulnerabilities for this project version.

Click the  icon in the table next to the vulnerability to expand the row. A brief description, additional information, and fields to remediate the vulnerability appear.

Click the  next to a component to open the Remediate Vulnerability modal. From here, you can update the following fields:

Status. See the table above for status definitions.

Status Justification. If "Known Not Affected" is the selected remediation, you must provide a justification for it. You can choose from the following:

Component not present. The vulnerable component is not included in the product.

Vulnerable code not present. The specific vulnerable code is not present in the component.

Vulnerable code cannot be controlled by adversary. The vulnerable code is present but cannot be controlled or exploited by an attacker.

Vulnerable code not in execute path. The vulnerable code exists but cannot be executed in the product's operational context.

Inline mitigations already exist. Built-in security measures are already in place, preventing the exploitation of the vulnerability.

Remediation: If "Known Affected" is the selected remediation, you must provide a remediation option. You can choose from the following:

Mitigation: The product includes built-in protections that prevent exploitation of the vulnerability.

No fix planned: The vulnerability will not be fixed.

None available: There are no fixes available for this vulnerability.

Vendor fix: There is an update by the vendor to address the vulnerability.

Workaround: There is a workaround available to fix the problem.

Target Date. This refers to the planned or intended deadline by which a vulnerability is expected to be remediated. It's often set based on the severity of the vulnerability, risk assessments, and your organization's security policies.

Actual Date. This is the date when the vulnerability is actually remediated or mitigated. It may differ from the target date depending on various factors, such as resource availability, complexity of the issue, or unexpected delays.

Comments. Any additional details or information regarding the vulnerability.

Remediating vulnerability by origin
To remediate vulnerabilities for this and/or additional project versions by origin, click the  icon in the table next to the vulnerability to expand the row and then click the View BDSA record or View CVE record link in the Description box. Doing so will open the vulnerability's BDSA record or CVE record page.

From here, you can view the projects affected by this vulnerability by selecting the Affected Projects tab. See the BDSA record or CVE record links above for more detailed instructions on how to remediate vulnerabilities by origin.

Note: When viewing projects on this tab, you may see rows that are hashed out and cannot be selected for remediation. This is due to the project having a linked type of security vulnerability record, either BDSA or CVE. If that vulnerability record is not prioritized in the Security Risk Ranking, a Remediation Plan cannot be undertaken for that project. Consider viewing the prioritized security vulnerability record to update the Remediation Plan.


===== TOPIC: Getting remediation guidance =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id fS5nXm8vhM4X_8~DWtE~jA)

When Black Duck identifies a component version with known security vulnerabilties, it attempts to find safer alternative versions of that component. These are presented as a Upgrade Recommendation within the component slide-out panel on the project version's BOM.

After reviewing this information, you may want to explore whether alternative component versions are available—particularly ones that resolves the security vulnerability affecting the version used in your BOM.

Upgrade recommendations
The simplest way to minimize or resolve security risk is to upgrade the version of the used component with fewer vulnerabilities.

If your project version contains any component versions which have known vulnerabilities or are simply out of date, the Upgrade Recommendation section will display options you can explore to mitigate risk:

Short-Term recommendations provides a short-term upgrade path as it is typically the same major version as the version currently used in your BOM.

Unlike the short term upgrade recommendation, Long-Term recommendations usually requires a major version upgrade. This may require more planning and/or engineering work to implement.

If the component is a transitive dependency, you will see two additional options, Direct Dependency and Component Version:

Direct Dependency: Provides a short- and long-term upgrade recommendation for the root node of a transitive dependency.

Component Version: Short-term typically reflects upgrading a component's minor or patch version. Long-term will focus on upgrading a component's major version.


===== TOPIC: Managing global remediation for a vulnerability =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id bSdveQyAmYj~cK1AhBDsDQ)

There may be a vulnerability that appears frequently in your BOMs. Instead of repeatedly reviewing and remediating that vulnerability, set a global default remediation status for it.

After you set a global remediation status, when that vulnerability appears in new BOMs, it will automatically get the global remediation status you defined.

Note: Any component in your existing BOMs that has that vulnerability retains its current remediation status. The global remediation status only applies to new instances of the vulnerability.

You must have the Global Security Manager role to set or remove a global remediation status for a vulnerability.

Setting a global remediation for a vulnerability

Use this process to set a global remediation status or edit an existing status.

Find the vulnerability you want to remediate globally, For example, you can: Use the Vulnerabilities tab for a specific project version.

Use the Search feature.

View the security record.

When viewing a list of vulnerabilities in a table, select > in the table next to the vulnerability to view a brief description. Then select either View BDSA record or View CVE record.

When using the Search feature, select the BDSA or CVE record in the search results.

Select the Settings tab.

Select a default status and optionally, enter a comment. This comment appears when viewing the description, as described below.

Click Save.

The Default Remediation Status Confirmation dialog box appears.

Click Confirm.

Clearing a global default remediation status

You can remove a global default remediation status. Clearing a status only affects future vulnerabilities: components with the existing global vulnerability status will retain that status. To modify the status of the existing vulnerabilities, modify the remediation status manually either individually or by using bulk remediation.

Find and display the vulnerability record as described in the previous section.

Select the Settings tab.

Click Clear.

The Default Remediation Status confirmation dialog box appears.

Click Confirm.

Viewing all vulnerabilities with global remediation

You can view all vulnerabilities with global remediation by selecting the Default Remediation filter when searching for vulnerabilities. Select the BDSA or CVE record number in the search results and then select the Settings tab, as described previously to view the remediation status.


===== TOPIC: VEX (global reports) =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id JTsbvpqnfr1Qr73fec5lPw)

Vulnerability Exploitability eXchange (VEX) reports in Black Duck SCA offer a standardized way to communicate the exploitability status of vulnerabilities in your products. These machine-readable reports help organizations efficiently inform stakeholders about whether specific vulnerabilities affect their offerings.

An SBOM (Software Bill of Materials) serves as a static declaration of components in a product release. After release, it's important to determine the exploitability of any vulnerabilities, and VEX reports facilitate this process. While the SBOM content remains unchanged, VEX allows for on-demand updates regarding the status of vulnerabilities for specific project versions.

Important: To take advantage of this feature, you must have Vulnerability Exploitability eXchange (VEX) enabled on your product registration key.

Creating a Global VEX Report
Global VEX reports summarize vulnerabilities across all projects in your Black Duck SCA environment, aiding in high-level assessments and remediation decisions. Follow the steps below to generate a global VEX report:

Click .

Click + Create new report. The Create New Report dialog box appears.

Select Vulnerability Exploitability EXchange (VEX): CSAF 2.0 from the Vulnerability Report Type list.

Select a project from the Projects field.

Select the desired Project Phases. The VEX report will include an entry for each CVE or BDSA within the selected project(s) as long as they have one of the following Black Duck SCA status values:

Under Investigation

Needs Review

Known Affected

Known Not Affected

Remediation Required

Remediation Complete

Select a Template.

Optionally, you can expand the Template Details section to see which options are enabled in the selected template.

Click Save to run the report.

The following links appear when the report completes:

csaf-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report.

Select the link to view the report.

VEX Report Format
The VEX report utilizes the CSAF 2.0 (profile 5) format, aligning with industry standards for vulnerability reporting. It clearly indicates which products are unaffected by vulnerabilities, making it a valuable resource for product security teams. This feature facilitates effective communication about security risks, enabling organizations to address customer inquiries and maintain a robust security posture.

Reports will be generated in JSON format, implementing only the minimum required elements for CSAF v2, profile 5. Each report will include entries for CVEs or BDSAs within the selected projects that have one of the following BD status values:

Under Investigation

Needs Review

Known Affected

Known Not Affected

Remediation Required

Remediation Complete

VEX Document Metadata
The VEX report includes essential metadata that is automatically populated and structured according to the CSAF 2.0 specifications. Below are the key elements of the VEX document metadata:

Document metadata

CSAF Version: Set to 2.0 (cannot be modified).

Category: Set to csaf_vex (cannot be modified).

Publisher

Category: Set to vendor (cannot be modified).

Name: Use the value from the existing Project Group SBOM Creator Organization field. If this field is set to the default value of "COMPANY NAME," a warning will be generated indicating that the default value is being used and should be changed. Users will have the option to Cancel or Continue:

Cancel: Returns to the report generation screen.

Continue: Generates the report using "COMPANY NAME" as the publisher name.

Namespace: A new text field will be added under the "Person" field in the Project Group SBOM fields for the Namespace. SBOM generation will utilize the BD namespace value to populate the namespace field in the SBOMs (for applicable SPDX/CycloneDX versions).

Title: Defined by Black Duck and currently not modifiable. The title will read: "Vulnerability status report using the CSAF 2.0 Profile 5 specification."

Tracking

ID: The ID will be the CSAF document filename (e.g., csaf-report_all_projects_2025-07-22_143038). The VEX Product ID can be configured in SBOM Fields.

Current Release Date: The date/timestamp of report generation (UTC).

Initial Release Date: The timestamp of report creation.

Revision History: One entry will be added for the current (latest) information:

Date: Report generation date/timestamp (UTC).

Number: Hardcoded value of 1 for the version.

Summary: Either "Latest information" or "Initial," depending on whether tracking both is necessary.

Version: Hardcoded value of 1 for the version.

Generator Information:

Date: Report generation date/timestamp (UTC).

Engine:

Name: "Black Duck HUB"

Version: The version of Black Duck HUB used to generate the report.

Status: Set to draft. (Note: Future support may be added for final and interim options, as referenced in section 3.2.1.12.7 of the CSAF 2.0 specification.)

Product Tree: The product_tree section of a VEX report in SCA provides a hierarchical representation of the products that are affected by a specific vulnerability. It is structured to illustrate the relationships between different product versions and their corresponding product names.

Branches: The product_tree consists of branches that represent different levels of the hierarchy. Each branch can contain further branches, allowing for a nested structure that captures the relationship between parent products and their versions.

Category: Each branch includes a category that defines the type of information it represents. In the example provided, categories might include "product_name" and "product_version."

Name: The name of the product or product version.

Product: Each product branch contains relevant details such as:

Name: The name of the product or product version.

Product ID: A unique identifier for the product, which helps in distinguishing it from other products within the tree.

Vulnerabilties: The Vulnerabilities section details specific vulnerabilities identified within the software components. This section is essential for understanding the security posture of the application and the associated risks.

CVE Identifier: If the vulnerability is a CVE, it is listed with its unique CVE ID (Common Vulnerabilities and Exposures). This identifier allows for easy tracking and reference to the vulnerability in external databases.

Notes: Accompanying each CVE entry are detailed notes that provide descriptions of the vulnerabilities. These descriptions explain the nature of the vulnerability, its potential impact, and any relevant technical details.

Category: Defines the type of note.

Text: The actual free-form text providing the information. If there is a related EUVD ID associated with this CVE, it will be displayed here.

Product Status: This section is essential for users to understand the current state of the products affected by vulnerabilities. It provides transparency regarding ongoing assessments and remediation efforts, helping organizations prioritize their actions to maintain security.

Scores: This section provides critical information regarding the severity of the identified vulnerabilities, utilizing the Common Vulnerability Scoring System (CVSS).

IDs: If the vulnerability has a BDSA ID, it will be found in this section.

Distribution

TLP:

Label: TLP label associated with the component version.

Notes: Provides additional information about the document itself. This can include general descriptions, frequently asked questions, summaries, or legal disclaimers.

Category: Note type identifier. Displays legal_disclaimer if the project group has a VEX Legal Disclaimer.

Text: The actual content of the legal disclaimer. Free-form text containing legal terms, conditions, limitations, and protections as defined by the organization.

VEX status mapping

Black Duck SCA Vulnerability Status
CSAF VEX Status

AFFECTED
known_affected

Duplicate
N/A - Not included in report

Ignored
N/A - Not included in report

MITIGATED
known_not_affected with the justification inline_mitigations_already_exist

NEEDS_REVIEW
under_investigation

NEW
under_investigation

NOT_AFFECTED
known_not_affected

PATCHED
fixed

REMEDIATION_COMPLETE
fixed

REMEDIATION_REQUIRED
known_affected

UNDER_INVESTIGATION
under_investigation

Notes:

The results were validated by generating VEX documents that have vulnerabilities with each of the Black Duck SCA status values that we have

The order of the Black Duck SCA Vulnerability Status in the table above is the order that is represented in the UI

The value in the CSAF VEX Status is the actual value in the report


===== TOPIC: How VEX Fields Are Determined in Global Reports =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id OL~Zc8_NVbcCv2RaO6jVtQ)

When you generate a global report that includes multiple projects from different project groups, Black Duck SCA uses a closest common ancestor approach to determine which values to use for VEX fields like legal_disclaimer and namespace.

What Does This Mean?
Black Duck SCA looks at the project group hierarchy and finds the nearest project group that is a parent (ancestor) to all selected projects. The VEX field values from that common ancestor project group are used in the report.

How It Works: Examples

Example 1: Direct Common Parent
Project hierarchy:

Root (Black Duck Project Groups)
└── Project Group C
├── Project Group A
│   └── Project 1
└── Project Group B
    └── Project 2When you select: Project 1 and Project 2

Common ancestor: Project Group C

Result: VEX fields from Project Group C are used in the report.

Example 2: Higher-Level Common Parent
Project hierarchy:

Root (Black Duck Project Groups)
└── Project Group D
    ├── Project Group C
    │   └── Project Group A
    │       └── Project 1
    └── Project Group B
        └── Project 2When you select: Project 1 and Project 2

Common ancestor: Project Group D

Result: VEX fields from Project Group D are used in the report.

Example 3: Single Project Selected
Project hierarchy:

Root (Black Duck Project Groups)
└── Project Group D
    └── Project Group C
        └── Project Group A
            └── Project 1When you select: Only Project 1

Common ancestor: Project Group A (the immediate parent)

Result: VEX fields from Project Group A are used in the report.

Example 4: No Shared Parent (Uses Root)
Project hierarchy:

Root (Black Duck Project Groups)
├── Project Group C
│   └── Project Group A
│       └── Project 1
└── Project Group D
    └── Project Group B
        └── Project 2When you select: Project 1 and Project 2

Common ancestor: Root (no other shared parent exists)

Result: VEX fields from the Root project group are used in the report.

Key Takeaways
Black Duck SCA finds the nearest project group that is a parent to all selected projects

VEX field values from that ancestor project group are applied to the report

If projects have no common parent, root-level VEX fields are used

For single-project reports, the immediate parent project group is used


===== TOPIC: Vulnerability Remediation report =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id K8qS_2qA2p7Nu66Urbx13A)

Based on a specific date range, the Vulnerability Remediation report lists all the vulnerabilities that match a specific remediation status.

For example, you can use this report to identify all of the vulnerabilities that require remediation or all the vulnerabilities that have been mitigated and ignored.

This report can be run at the global level (for all projects to which you have access) or for one or more projects to which you have access. It can also be run at the project version level to view this information for a specific project version.

Running a Vulnerability Remediation report at the global level
To run a Vulnerability Remediation report at the global level:

Click .

Click + Create new report. The Create New Report dialog box appears.

Select Vulnerability Remediation Report from the Report Type list.

To run the report for selected projects, enter one or more project names in the Projects field. Leave the field blank to create the report for all projects to which you have access.

Select either HTML or CSV as the report format.

Tip: Use the CSV option when your data becomes too large to render and view in the browser.

Select the dates for this report. The date represents the day when the vulnerability was published. By default, the end date is the current date.

Optionally, select one or more remediation statuses.

Click Confirm to run the report. One of the following links appears when the report completes:

vulnerability-remedation-report_all_assigned_projects_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report

vulnerability-remedation-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for one or more projects

Reports for a specific project can be accessed by any user who is a member of the project. However, if the report contains multiple projects, the user must be a member of all projects to access the report.

Select the link to view the report.

If you selected CSV as the report format, download the report and extract the zip file.

Note: You can use the native print functionality of your web browser to print the HTML version of the report.

Running a Vulnerability Remediation report at the project level
To run a Vulnerability Remediation report at the project level:

Click the desired project name on the Dashboard.

Click the desired project version.

Click the Reports tab.

Click + Create new report. The Create New Report dialog box appears.

Select Vulnerability Remediation Report from the Report Type list.

To run the report for selected projects, enter one or more project names in the Projects field. Leave the field blank to create the report for all projects to which you have access.

Select either HTML or CSV as the report format.

Tip: Use the CSV option when your data becomes too large to render and view in the browser.

Select the dates for this report. The date represents the day when the vulnerability was published. By default, the end date is the current date.

Optionally, select one or more remediation statuses.

Click Confirm to run the report. One of the following links appears when the report completes:

vulnerability-remedation-report_all_assigned_projects_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report

vulnerability-remedation-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for one or more projects

Reports for a specific project can be accessed by any user who is a member of the project. However, if the report contains multiple projects, the user must be a member of all projects to access the report.

Select the link to view the report.

If you selected CSV as the report format, download the report and extract the zip file.

Note: You can use the native print functionality of your web browser to print the HTML version of the report.


===== TOPIC: Vulnerability Status report =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id Q~FRF6d7wQ4gb4FpT5BIgw)

The Vulnerability Status report includes all the vulnerabilities that are associated with the projects and project versions to which you have access.

For example, you can use this report to identify which projects are secure and which projects and project versions contain security risks.

This report can be run at the global level (for all projects to which you have access) or for one or more projects to which you have access. It can also be run at the project version level to view this information for a specific project version.

Running a Vulnerability Status report at the global level
To run a Vulnerability Status report at the global level:

Click .

Click + Create new report. The Create New Report dialog box appears.

Select Vulnerability Status Report from the Report Type list.

To run the report for selected projects, enter one or more project names in the Projects field. Leave the field blank to create the report for all projects to which you have access.

Select either HTML or CSV as the report format.

Tip: Use the CSV option when your data becomes too large to render and view in the browser.

Click Confirm to run the report. One of the following links appear when the report completes:

vulnerability-status-report_all_assigned_projects_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report

vulnerability-status-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for one or more projects

Reports for a specific project can be accessed by any user who is a member of the project. However, if the report contains multiple projects, the user must be a member of all projects to access the report.

Select the link to view the report.

If you selected CSV as the report format, download the report and extract the zip file.

Note: You can use the native print functionality of your web browser to print the HTML version of the report.

Running a Vulnerability Status report at the project level
To run a Vulnerability Status report at the project level:

Click the desired project name on the Dashboard.

Click the desired project version.

Click the Reports tab.

Click the + Create New Report.

Select Vulnerability from the report list.

Select Vulnerability Status Report from the Report Type list.

To run the report for selected projects, enter one or more project names in the Projects field. Leave the field blank to create the report for all projects to which you have access.

Select either HTML or CSV as the report format.

Tip: Use the CSV option when your data becomes too large to render and view in the browser.

Click Confirm to run the report. One of the following links appear when the report completes:

vulnerability-status-report_all_assigned_projects_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report

vulnerability-status-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for one or more projects

Reports for a specific project can be accessed by any user who is a member of the project. However, if the report contains multiple projects, the user must be a member of all projects to access the report.

Select the link to view the report.

If you selected CSV as the report format, download the report and extract the zip file.

Note: You can use the native print functionality of your web browser to print the HTML version of the report.


===== TOPIC: Vulnerability Update report =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id RgDsoHW5qptnt_N5grSzLg)

Based on a specific date range, the Vulnerability Update report includes the following information for projects to which you have access:

New vulnerabilities. For example, you can use this report to identify new vulnerabilities after code or a Docker image has been rescanned.

Updates to the remediation status of existing vulnerabilities. For example, you can use this report to track the progress of a remediation effort.

Updates to any of the data that is associated with vulnerabilities.For example, you can use this report to identify if the risk scores associated with existing vulnerabilities have changed.

This report can be run at the global level (for all projects to which you have access) or for one or more projects to which you have access. It can also be run at the project version level to view this information for a specific project version.

Running a Vulnerability Update report at the global level
To run a Vulnerability Update report at the global level:

Click .

Click + Create new report. The Create New Report dialog box appears.

Select Vulnerability Update Report from the Report Type list.

To run the report for selected projects, enter one or more project names in the Projects field. Leave the field blank to create the report for all projects to which you have access.

Select either HTML or CSV as the report format.

Tip: Use the CSV option when your data becomes too large to render and view in the browser.

Select the dates for this report. The date represents the day on which the vulnerability was added to a project version or the information associated with the vulnerability was updated. By default, the end date is the current date.

Click Confirm to run the report. One of the following links appear when the report completes:

vulnerability-update-report_all_assigned_projects_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report

vulnerability-update-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for one or more projects

Reports for a specific project can be accessed by any user who is a member of the project. However, if the report contains multiple projects, the user must be a member of all projects to access the report.

Select the link to view the report.

If you selected CSV as the report format, download the report and extract the zip file. The CSV report will contain four reports:

new-remediated-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all new remediations for the selected project(s) within the specified time frame. A vulnerability is newly remediated if the remediation was created after the vulnerability was created and it is in the specified time range.

new-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all new vulnerabilities for the selected project(s) within the specified time frame. A vulnerability was associated to a BOM component whether or not it is remediated and the bom association was in the specified time range.

updated-remediated-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all updated remediations for vulnerabilities that occurred within the specified time range for the selected project(s). A vulnerability has an updated remediation if the remediation update happened after the remediation was created and is in the specified time range.

updated-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all updated vulnerabilities for the selected project(s) within the specified time frame. A vulnerability is updated if the the updated dateTime is within the specified time range and this vulnerability risk was updated after the risk was created.

Note: You can use the native print functionality of your web browser to print the HTML version of the report.

Running a Vulnerability Update report at the project level
To run a Vulnerability Update report at the project level:

Click the desired project name on the Dashboard.

Click the desired project version.

Click the Reports tab.

Click + Create new report. The Create New Report dialog box appears.

Select Vulnerability Update Report from the Report Type list.

To run the report for selected projects, enter one or more project names in the Projects field. Leave the field blank to create the report for all projects to which you have access.

Select either HTML or CSV as the report format.

Tip: Use the CSV option when your data becomes too large to render and view in the browser.

Select the dates for this report. The date represents the day on which the vulnerability was added to a project version or the information associated with the vulnerability was updated. By default, the end date is the current date.

Click Confirm to run the report. One of the following links appear when the report completes:

vulnerability-update-report_all_assigned_projects_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for a global version of the report

vulnerability-update-report_YYYY-MM-DD_HHMMSS (time stamp in system timezone) for one or more projects

Reports for a specific project can be accessed by any user who is a member of the project. However, if the report contains multiple projects, the user must be a member of all projects to access the report.

Select the link to view the report.

If you selected CSV as the report format, download the report and extract the zip file. The CSV report will contain four reports:

new-remediated-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all new remediations for the selected project(s) within the specified time frame. A vulnerability is newly remediated if the remediation was created after the vulnerability was created and it is in the specified time range.

new-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all new vulnerabilities for the selected project(s) within the specified time frame. A vulnerability was associated to a BOM component whether or not it is remediated and the bom association was in the specified time range.

updated-remediated-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all updated remediations for vulnerabilities that occurred within the specified time range for the selected project(s). A vulnerability has an updated remediation if the remediation update happened after the remediation was created and is in the specified time range.

updated-vulnerabilities_YYYY-MM-DD_HHMMSS.csv

This report will contain all updated vulnerabilities for the selected project(s) within the specified time frame. A vulnerability is updated if the the updated dateTime is within the specified time range and this vulnerability risk was updated after the risk was created.

Note: You can use the native print functionality of your web browser to print the HTML version of the report.


===== TOPIC: Analyzing the impact of a vulnerability =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id zXXuMi_EGdi6wLsXykf_cw)

If a project version has several vulnerabilities, how can you decide which vulnerability you should focus on first?

To help you to prioritize which vulnerabilities you should address first, Black Duck can determine if any external public methods called by your Java applications are potentially involved in a known vulnerability. Black Duck can identify the called fully qualified public functional names in your source code and match them to the known function names being exploited by a vulnerability. By knowing whether any external public methods called by your Java applications are potentially involved in a known vulnerability, you can prioritize what vulnerabilities you need to concentrate on.

Vulnerability impact analysis works with Black Duck Security Advisories (BDSAs), a Black Duck-exclusive vulnerability data feed. Vulnerability metadata has been added to BDSAs that includes the fully qualified public function names that expose the vulnerability. Using this data, Black Duck can determine if vulnerable code is more likely to be invoked, and flags those vulnerabilities as reachable, indicating to you that these vulnerabilities are a higher priority for remediation.

Important: Vulnerability impact analysis can help you triage vulnerabilities in open source components. It is not a definitive list of the vulnerabilities that do or do not affect your code. Although Black Duck may indicate that a vulnerability is reachable, it does not indicate that the vulnerability definitely affects your code, as your code may not trigger the vulnerability. 

Likewise, Black Duck may not denote that a vulnerability is reachable. However, that does not indicate that your code is safe from the vulnerability as Black Duck may not have data for a specific vulnerability.

Vulnerability impact analysis process

The process to display the possible impact of a vulnerability in Black Duck is:

1. Black Duck Detect analyzes the code

When the --detect.impact.analysis.enabled property in Black Duck Detect to set to true, Black Duck Detect creates a call graph (a list of calls made by your code) to understand the public methods your code is using in your application. The call graph shows the fully qualified public method names as well as the line number where the function was called.

Along with creating BOM files, Black Duck Detect creates a file which will be used by Black Duck KnowledgeBase for matching call graph signatures against BDSA-provided function signatures. This file is encrypted with SHA1 hashes. Hashing of the call graph signatures is completed at the client system.

The data is packaged into a single file and Black Duck Detect sends the file over HTTPS to the Black Duck server.

2. Black Duck sends data to the KnowledgeBase

Black Duck sends the hashed call graph function signatures to Black Duck KnowledgeBase via a Black Duck KnowledgeBase API.

3. Black Duck KnowledgeBase identifies vulnerable methods

The Black Duck KnowledgeBase uses the Function Signature Match Service to compare the hashed call graph signatures to KnowledgeBase hashed data for BDSA vulnerabilities with associated fully qualified public method names metadata. Fully qualified public method name matching is similar to signature matching: a discovered set of fully qualified public method names is compared against those known to the Black Duck KnowledgeBase.

The Black Duck KnowledgeBase sends the vulnerability metadata (vulnerable methods) to the Black Duck server via HTTPS.

4. Black Duck identifies vulnerabilities

Black Duck creates the data that needs to persist in the Black Duck PostgreSQL database. The data is stored as a new scan type (Vulnerability Impact) in Black Duck.

Black Duck cross references the identified methods with the vulnerable methods from BDSA to identify which vulnerabilities the user is calling in their code.

Black Duck displays the vulnerabilities for a component that have a method that is being called in the project version's Vulnerabilities tab.

Viewing reachable vulnerabilities

To view reachable vulnerabilities:

Set the --detect.impact.analysis.enabled property in Black Duck Detect to true to enable vulnerability impact analysis.

Once scanning completes and Black Duck has built the BOM, open the project version's Vulnerabilities tab which lists the security vulnerabilities for this project version.

Select a vulnerability from the table to view a table which lists the vulnerabilities for this component.

 located next to the BDSA record number indicates that there is a function call in your code that makes this vulnerability reachable. Use the Reachable filter to view all such BDSA records.

Click  to view more information for an individual BDSA record.

The Reachable Vulnerability dialog box lists:

Component name and version

BDSA record

A list of all vulnerable function calls in your code.

Select a function name to view the method name and line number in your code.

Note the following:

This feature is available in Black Duck Detect version 6.5 or later (and Black Duck Detect Desktop that uses Black Duck Detect 6.5 and later). Set the --detect.impact.analysis.enabled property in Black Duck Detect to true to enable vulnerability impact analysis.

This feature is for Java applications only. Black Duck Detect looks at Java .class files only.

Black Duck Detect only discovers vulnerabilities in public methods that call potentially vulnerable functions.

This feature displays reachable functions for BDSAs only.

There is a project version report,vulnerability_matches_date_time.csv, that lists the component, vulnerability data, and vulnerability impact analysis data for each component potentially reached by a vulnerability.

A vulnerability condition, Reachable from Source, is available enabling you to create policy rules for vulnerabilities which has been identified as reachable. Use this condition to create policy rules that prioritize those vulnerabilities.
