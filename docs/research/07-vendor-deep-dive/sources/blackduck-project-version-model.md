# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/1WqD3iF0wWDzpOGfy2mr8Q
# Reader base: https://docs.blackduck.com/bundle/blackduck-hub/page/
# Captured: 2026-09-21



===== TOPIC: Understanding projects in Black Duck =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id h80x53_B_0Bdz169QXgRDQ)

Black Duck helps project teams manage project information and the OSS components that are being used in each of the versions of a project.

At the project level, team members can:

Update the project and project version information.

This information is searchable in Black Duck.

Manage tags associated with the project.

This information is searchable in Black Duck.

Create a new version of the project.

Manage project team membership.

Delete a project or project version.

The My Projects dashboard lists all projects where you are a member or where you have project-group privileges. Select the name of the project to go to the Project Name page which displays the Overview tab by default.

This tab provides the following information for each version in this project:

Column
Description

N/A
Icons shown to the left of the version name:

Policy violation. Select the icon to view information on the policy violation.

 Policy violation has been overridden.

Select the icon to view information on the policy violation.

Version
Name of the project version.

Phase
The development phase of this version. The possible values are:

In Planning

In Development

Pre-release

Released

Deprecated

Archived

The value in this field is used to calculate risk for the project. Archived versions are not included in project risk calculations. Click here for more information about project version phases.

Last Updated
When this project version was last updated. Hover over the value to see:

When the scan mapped to this version of the project was last scanned. If there are multiple scans mapped to this version of the project, this is when any of those scans was most recently scanned.

When the BOM was last updated. There are several ways that the BOM could have been updated, including manual adjustments, new scans of existing code or Docker images, and newly-mapped scans.

Last Scanned
Date of the last scan for this project version. Hover over the value to see the date and time.

License
Name of the license for this project version.

Security Risk
Bars show the critical, high, medium, and low security risk levels for the OSS components in this version of the project.

Select the bar to view the number of affected components.

License Risk
Bars show the high (100% red), medium (50% red), and low (100% gray) license risk levels for the OSS components in this version of the project.

Select the bar to view the number of affected components.

Operational Risk
Bars show the high (100% red), medium (50% red), and low (100% gray) operational risk levels for the OSS components in this version of the project.

Select the bar to view the number of affected components.

Above the table, the following information is shown:

Description. Description of this project. Select the Settings tab to create or revise the description.

Created. The user who created this project and the date it was created.

Updated. The user who last updated this project (by modifying any project information or by adding a member) and the date it was last updated.

Updates do not include adding or modifying a project version.

Tags. Any tags for this project.

Additional Fields. Project custom field information.


===== TOPIC: About project versions =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id HVIl7rdYLsppcoMxwWSxbA)

Use the Overview tab to obtain information about a project version.

This tab provides the following information:

The Where Used table lists the project name, project version, tier, release date, distribution, and phase for all projects where this project version is a subproject.

To the right of the table, the following information is shown:

Description. Description of this project. Select the Settings tab for the project to create or revise the description.

Licenses. The license(s) associated with this project version.

Created. The user who created this project version and the date it was created.

Last Settings Updates. The user who last updated this project version settings and the date it was last updated.

Last Scan. Date and time the latest scan(s) mapped to this project version completed.

Last BOM Update. Date and time of the last BOM update.

Tags. Any tags for this project version.

Custom Fields. Any custom fields for this project version.

To view the project version Overview tab:

Select the desired version name.

Select the Overview tab.


===== TOPIC: About project version phases =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id QHsfgv6i9uJjROaE~MNDtA)

Projects versions include a phase which you can use to manage your development projects in Black Duck. Possible phase values are:

In Planning: The In Planning phase is where the project solution is further developed in as much detail as possible and the steps necessary to meet the project’s objective are planned.

In Development: The In Development phase is when the project plan is put into motion and the work of the project is performed.

Pre-release: The Pre-release phase is when the project development has been completed and testing is underway.

Released: The Released phase is when the project has officially progressed to general availability and the software product is ready to be delivered or has been delivered.

Deprecated: The Deprecated phase is when the software has reached end-of-life and is no longer sold or supported. In this phase, the software might still be used by customers.

Archived: The Archived phase is similar to the Deprecated phase, however the software is no longer available and customers are no longer utilizing it, having moved on to more recent releases.

Note: The definitions above serve only as examples. You can use the phases in any way to suit your organization's software development life cycle steps.

You can select the phase when creating or editing a project version. By default, a project version is in the "In Planning" phase.

Black Duck treats In Planning, In Development, Pre-release, Released, and Deprecated project versions the same. Black Duck does not differentiate between these phases: these phases are to help you manage your projects. Project versions with these phases are included in project risk calculations.

Archived project versions are treated differently than the other project version phases.

Note: You can "lock" a project version BOM against any component and license changes from Black Duck KnowledgeBase by select the archived phase, as described below.

About archived project versions
You can modify archived project versions, as you would a project version in any other phase, for example, modifying component usage and licenses.

However, archived project versions are treated differently than all other project version phases.

Archived project versions are excluded from project risk calculations.

Project versions with any other phase are included in project risk calculations.

If you enabled persistent edits:Your edits made to a project version are not propagated to archived project versions.

Your edits made to an archived project version are propagated to all other non-archived project versions.

Those edits are not applied to any other archived project version.

Updates from Black Duck KnowledgeBase regarding security vulnerabilities are applied to archived project versions.

Other updates from Black Duck KB, such as updates to license information, are not applied to archived project versions.

New policy rules and updated expressions are not evaluated in archived project versions.

Disabled and deleted policy rules violations will be removed from archived project versions.


===== TOPIC: About Long-Term support (LTS) projects =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id APkYTFtOKsJysVQLwRuTzA)

Long-Term Support (LTS) project versions enable tracking of vulnerability data for released product versions. LTS projects are intended for software already in use by end users or customers. Designed with scalability in mind, LTS projects can support extremely high volumes of project versions.

LTS project versions retain minimal data from Active project versions, focusing on tracking newly discovered vulnerabilities in the components within the LTS Bill of Materials (BOM). When converting an Active version to LTS, a Software Bill of Materials (SBOM) is automatically created to facilitate sharing with required third parties. While LTS version do not currently support notifications, they will receive new vulnerability data as it is published to the Black Duck KnowledgeBase.

Note: Converting a project version to LTS is a one-way process and cannot be reverted once started.

Converting a project version to LTS


===== TOPIC: Converting a project version to LTS =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id w9JuuqT_KALwG8GjoDUY1g)

Long-Term Support (LTS) project versions are designed to track new vulnerabilities for released software artifacts. They are not intended for use by developers or workflows related to application development or compliance workflows.

LTS versions omit project and scan data. This includes:

Source file information

Scans and all information related to match types

Snippets

IaC results, unmatched component data, and malware information

Comments

License conflicts, copyrights, and deep license data

Vulnerability triage information

BOM custom fields

Important considerations before converting your project versions to LTS
Converting from an LTS version back to Active is not currently supported.

AI models are not retained.

Custom component vulnerability associations are preserved during LTS conversion. If a custom component version is associated with vulnerabilities through a valid CPE 2.3 identifier, those vulnerabilities remain available in the LTS project version.

Vulnerability records with multiple remediation origins and different statuses will be merged during conversion. The most severe remediation status among the merged records will be retained.

Comments from all merged remediation records will be concatenated into a single consolidated comment. This normalization is intentional and ensures consistency in the LTS model, which does not support remediation information at the origin level.

This behavior reflects the transition from origin-based remediation tracking to the LTS model’s component-version-based approach and applies when converting active projects to LTS.

How to convert a project version to LTS
To convert a project version to LTS status:

Click  for the desired project version and select Convert to LTS.

Configure the SBOM report that will be generated during the conversion process:

Select a SBOM Template. You can expand the Template Details section to view the enabled fields which will appear in the SBOM report.

Select a SBOM specification and report format.

Click Convert.

Once the conversion is complete, the project version will be moved from the Active Versions tab of project versions to the Long-Term Support (LTS) Versions tab.


===== TOPIC: About project version BOMs =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id RUMsYSpaZ7OyP1vtDAQDCw)




===== TOPIC: Applying adjustments to all versions of a project =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id YOA6_7o6fw494s6NFkrPaA)

You can select whether adjustments to a component apply to a specific version of a project or if adjustments apply to all versions of a project.

What is the Component Adjustments setting?
Component Adjustments in the Project settings ensures that adjustments made to components are consistently applied across all versions of a project. However, it is important to understand how this setting interacts with manually added components.

Functionality of Component Adjustments
When you make adjustments to components that are shared across multiple project versions, those adjustments will be applied to all versions where the component exists. This means that if you mark a component as ignored in one project version, it will also be ignored in all other versions of that project where the component is present.

If you enable Component Adjustments then adjustments apply to all existing versions of a project, excluding archived versions of projects and manually added components, and will also be carried forward as additional scans are completed at the same code or Docker image.

For example, if you edit a matched component to a different component, then all other versions of the project that have that same matched component will have the match adjusted and all versions going forward will also have this match adjusted.

Manual Addition of Components
If a component is manually added to a specific project version, it does not automatically create a corresponding entry in other project versions. Each project version needs to have the component manually added if it is not already present. However, once a component is added to multiple versions, any further adjustments will apply universally to all instances of that component.

Note: There are instances when adjustments may not propagate to all versions. See Component Adjustment examples below.

Component Adjustments are enabled by default when you create a project.

CAUTION:
Please exercise caution when changing this option in order to avoid the Component Adjustment examples below. Projects created prior to release 3.1.0 will have this feature disabled by default. See the examples described below as those results will apply If you enable this feature to those projects.

When you edit a component (using the BOM or Source page), a  appears in the table row to indicate that a manual adjustment was made to this component:

Note: A  appears on the BOM page for any edits that you make to a BOM.

There is also the option of cloning project versions which enables you to baseline a project version.

Component Adjustments examples
Component Adjustments may appear to work differently than expected depending on the status of persistent edits and when the adjustments are made.

In the examples below, a project has several versions, none of which are archived.

Table 1. Scenario 1Steps
Example
Final Result

Component Adjustments are enabled.

 
 

An adjustment is made to an item in a component in one version of the project.

The license for Component A is changed in Version 1 of the project.

The adjustment is propagated to all versions of the project.

Component Adjustments are then disabled.
 
 

An adjustment is made to the same item in Component A in a version of the project.
The license for Component A is changed in Version 1 (or Version 2) of the project.
Although Component Adjustments are disabled, the edit is propagated to all versions of the project as the original adjustment was made when Component Adjustments were enabled.

Table 2. Scenario 2Steps
Example
Final Result

Component Adjustments are disabled.
 
 

An adjustment is made to an item in a component in one version of the project.
The license for Component A is changed in Version 1 of the project.
The adjustment appears in only Version 1 of the project.

Component Adjustments are then enabled.
 
 

An adjustment is made to the same item in the same component in the same version.
The license for Component A is changed again in Version 1 of the project.
The adjustment is applied to only that version of the project (Version 1 in our example). The adjustment does not propagate to other versions of the project as the original adjustment was made when Component Adjustments were disabled.

Table 3. Scenario 3Steps
Example
Final Result

Component Adjustments are disabled.
 
 

An adjustment is made to an item in a component in one version of the project.
The license for Component A is changed in Version 1 of the project.
The adjustment appears in only Version 1 of the project.

Component Adjustments are then enabled.
 
 

An adjustment is made to the same item in a component in a different version of the project.
The license for Component A is changed in Version 2 of the project.
The adjustment is propagated to all versions except Version 1.

Enabling or disabling Component Adjustments for a project

Select the Settings tab.

Check or uncheck the Component Adjustments check box to enable or disable persistent edits. Archived project versions and manually added components are excluded.

Click Save.


===== TOPIC: Cloning project versions =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id B3K2Gt7Wp4gw7nv7ftMj~A)

When creating a new project version, Black Duck SCA lets you select an existing project version and clone its component edits, remediation details, and/or license term fulfillment status to the new project version. Use cloning to help reduce your workload by using the analysis and resolutions you defined in an existing project version as a baseline for a new version.

Unlike persistent edits which synchronizes edits made in one version to all other versions of that project, edits made to the baseline version do not propagate to the cloned version. This gives you the ability to experiment with the cloned version while keeping the original version intact. Note that if you have enabled persistent edits, then edits made to the baseline version will be propagated to the cloned version.

To successfully use cloning:

Enable cloning, as described below.

Run a scan to the new version.

Cloned information appears in the cloned project version for components that are the same as in the original project version: if a component is not included in the newly scanned files, then that component will not be included in the new cloned project version. Cloned information will appear in the cloned project version for components that were manually added in the original project version.

By default, all options are cloned:

Additional Fields: Custom field information.

Component Edits:

Component and/or version information

Review flag

License

Usage

Ignored components

Comments

Manually added components

Confirmed snippet adjustments

Policy violation overrides and comments

Deep License Data

Remediation Details:

Remediation status

Target date

Actual date

Remediation comments

License Fulfillment Status. For license terms requiring fulfillment:

Fulfillment status (fulfilled or unfulfilled)

For fulfilled license terms, the user who fulfilled the term and the date it was fulfilled

Version Settings:

License

Notes

Nickname

Release Date

Phase

Distribution

Note: Cloning a project version in the Archived phase will not retain the Archived status. The cloned version will default to the In Development phase.

You can modify these settings by using the Cloning section in the Project Details section of the Settings tab of a project, as described here.

Note: You cannot clone individual component or remediation values.

Enabling cloning
You enable cloning:

Select Clone for the version you wish to clone from the Project Name page. The version of the Clone Version dialog box that appears depends on whether Version Settings was selected as a cloning attribute for the project:If Version Settings was selected, specify the version name in the Clone Version dialog box and click Clone.

If Version Settings was not selected, specify the version name in the Clone Version dialog box, enter any of the other project version settings, and click Clone.

Use the --cloneFrom parameter when using the command line to scan and create a project version.


===== TOPIC: Managing subprojects =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id mN0AxGWboyoX733rDxHzvQ)

[HUB-9934, 1452]You may have applications that include code from other projects, for example, a user management module that is included in several other applications. You can see risk information about the user management module as a project with its own BOM but may also want to see the same information in the BOM for every application that uses that module without having to re-scan the code.

Adding projects to your application's BOM gives you a complete view of this application and all associated risks, including vulnerabilities, license, and operational risk.

For these subprojects:

You must have permission to the project to add it to the BOM.

Users who do not have permission to the subproject will not be able to drill down to view additional data about that project version.

Modifications made to a project outside of the BOM will propagate to the subproject in the BOM. For example, if additional scans are completed for scans mapped to this project, those changes will propagate to the subproject.

An exception to this is the subproject version license: edits made to the project version license may or may not propagate to the license shown for the subproject in the BOM:

If you modify the project version license outside of the BOM and have not edited the subproject license from within the BOM, the edited license will appear in the BOM for the subproject.

If you modify the project version license outside of the BOM and have edited the subproject license from within the BOM, the license edit will not appear in the BOM for the subproject.

If you modify the subproject version license from within the BOM, that change is not propagated outside of the BOM.

Policy violations within the subproject will not appear in the BOM. However, a policy violation will appear in the BOM for the subproject if a policy rule is violated at the project level. For example, if you specified a policy rule that triggers a violation for unknown licenses and the project is added to the BOM with an unknown license, a policy violation will be triggered for that subproject.

Subprojects and their associated licenses are included in the Notices File report. You can exclude the subproject from the Notices File report.

Subproject security risks are added to the sum in the parent project.

You cannot add a Project Version to itself. However, you can add a Project Version to another version of the same project, provided that this addition does not create a dependency cycle.

To add a subproject:

Select the version name to open the Components tab.

Click Add and select Project to open the Add Project dialog box.

Enter the name and version of the project.

Note: You must have permission to the project to add it to the BOM.

Optionally add a license for this project or modify the existing license. If you do not enter a license, "Unknown License" appears in the BOM for the license for this project. The license selected for the subproject will determine its license risk.

Click Save.

Black Duck adds the selected project to the BOM.

To edit a project:

Select the BOM as described in the previous section.

Click and select Edit to open the Edit Component dialog box.

Select one or more different values and click Update.

To delete a subproject from a BOM:

Select the BOM as described in the previous section.

Click and select Delete to open the Delete Component dialog box.

Click Delete.

The BOM is updated and the risk is recalculated.

To view where projects are included as subprojects:

The Where Used table lists the projects where this project version is included in the BOM.

Locate the project using the Projects tab on the Dashboard by selecting the name of the project to go to the Project Name page.

Select the version name which opens the Components tab.

Select the Details tab to view where this project version is included as subprojects.

The Where Used table lists the project name, project version, tier, release date, distribution, and phase for all projects where this project version is a subproject.


===== TOPIC: Managing Project Groups =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id rNnHYEWOs8dKimUnn7Dauw)

Black Duck provides the ability to logically group all your projects in the Hub, allowing you to organize which projects belong to which business unit making it easier for you to view risk across the organization. Project groups can contain both projects and other project groups to provide a multi-level hierarchy.

To manage project groups:

Click  and select Project Groups.

From the Project Group Management page, you will see the root project group for all projects and groups.

Project Group Hierarchy

The top level of the hierarchy, or the root level, is the main level for all subsequent projects and project groups for your organization. By default, it is named "Black Duck Project Groups", but can be changed at any time.

Ancestor, Parent, and Child Projects and Project Groups

In the example above, you can see a number of levels which may act as individual projects or other project groups. Projects 1, 2, and 3 are considered children of the root level project group. The same can be said for Project 4 and Project 5 in relation to Project 3. Project 5 is also a child of Project 4.

The inverse relationship is called a parent. For example, Project 4's parent is Project 3 and Project 5's parent is Project 4.

An ancestor is any project group existing above the parent for that project group. Project 3 is an ancestor of Project 5.

Members and User Groups

The relationship between projects and project groups matters when assigning members and user groups to project groups. Members and user groups can be assigned to project groups with any number of roles. That assignment will give those users access to the project or project group they are directly assigned to (Direct Access), and to all child projects and project groups of that group with the specified roles unless that assignment is explicitly overridden at the lower levels (Indirect Access). This concept allows for setting users with default access to projects that haven't been created yet. For more details regarding user roles, see Understanding roles.

In the example above, users Bom and Copyright have been added as members with Direct Access. The sysadmin user is a member of the root level project group, therefore has Indirect Access to all child projects and project groups, including Project 3.

As a result, users Bom and Copyright now have Indirect Access to Project 4 as seen above. This extends to all children of Project 3. They will hold the same role for all child projects and project groups of Project 3.


===== TOPIC: Changing the project's SBOM alias =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id 6avw9nBW8KACqNNYWNjF3Q)

You can override project name and version info field at the project level.

Select the Settings tab.

Select SBOM Fields.

Enter a new project name in the Name field.


===== TOPIC: Mapping a scan to a project =====
# URL: https://docs.blackduck.com/bundle/blackduck-hub/page/ (topic id HNzm1lZjiI7LFO8WKc79dA)

Mapping a scan adds the scan data to the BOM of a project version.

Note: You can scan a Docker image or file directory location or archive more than once, but you only have to map it to a project version once. The host and path may be changed, but as long as code location name is the same, Black Duck automatically updates the BOM of the project with any new information discovered during subsequent scans.

To map a scan to a project:

Click .

Do one of the following:Click  and select Map to Project in the row of the scan that you want to map.

Select the path of the scan you want to map to open the Scan Name page.

Start typing the name of a project to progressively display matches in the Project field.

If necessary, select Create Project to create a new project and version.

Select the project version to which you want to map the component scan.

If necessary, select Create Version to create a new version for a project.

Click Save.

Black Duck displays the name and version of the project to which you mapped the component scan. Select the link to open the BOM page.

Note: Black Duck displays an aggregate project version BOM. If a component version appears more than once in an archive, it is only displayed in the BOM once.
