# Raw capture from docs.blackduck.com (khub API)
# Map: https://docs.blackduck.com/api/khub/maps/xmDr3Yryk7OYDGb__OGKlg
# Reader base: https://docs.blackduck.com/r/blackduck-signal/latest/
# Captured: 2026-09-21



===== TOPIC: Overview of Black Duck Signal =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id dB8K2SDHD53lShGOyuhOKg)

Signal introduces a new approach to application security, designed for agentic software development. We coupled Large Language Models with the Black Duck KnowledgeBase™, a repository containing more than 20 years of expert-vetted security insights, and together they deeply analyze software in ways not possible before.

Signal integrates directly with AI coding assistants and focuses on high-fidelity, high-priority issues most likely to be exploited. It works at machine speed and secures apps with minimal human effort.

What it can do
Find and fix issues in code, whether the code was written by humans or agentic AI. Signal can work with coding assistants like Gemini, Copilot, and Claude.

Let you decide whether to scan your code changes or the entire codebase. 

Scan any programmatic language. Because it is LLM-based, it can discover bugs in any language and doesn’t need any configuration to get started. It’s ideal for scanning languages that your other tools don’t support. 

Find bugs that would go undetected by rule-based engines.

Suggest fixes. Signal output includes guidance that AI agents can use to fix the code.

The use cases
 You can use Signal in two ways: Scan only your code changes, the way you would in a pull request

Scan all the code in your project.

Signal comes in two varieties: Developer and Enterprise. You should choose the variety that matches your workflow.

Table 1. Developer versus EnterpriseScenario 
Signal Developer
Signal Enterprise

Scan code owned by one contributor with the help of Agentic AI. Report only the issues owned by that contributor.
Yes
Yes

Scan code in an entire project. Easily add AI scans to existing automated workflows. 
No
Yes

Signal operating system support
Signal runs on these operating systems. linux-arm64

linux-x86_64

macos-arm64 

macos-x86_64 

windows_x86

Language support
Signal scans code effectively in any language. 

Traditional SAST tools define what they can analyze by maintaining rules for each language and framework they support. Signal works differently. It analyzes code based on semantics — meaning, structure, and context — reasoning about it the way a security engineer would, regardless of the language or frameworks used. This means Signal isn’t bound by a fixed list of supported languages; it understands your code on its own terms.


===== TOPIC: Get Started with Black Duck Signal =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id pWh4HdADYtbOrBKc4~5pUw)

There are different approaches to start using Signal. Select the approach that best matches your needs and preferences to start scanning your code:

Signal CLI: Use Signal directly from the command-line and get a SARIF report. For more details, see Signal CLI.

Coding Assistants: Configure the Signal MCP server and start scanning your code with Coding Assistants support.

Code Sight integration: Scan active files and code changes using improved analysis options, including dataflow detection and removing invalid or redundant findings, reducing the incidence of false positives with Signal and Code Sight VS Code Extension.

Bridge and Polaris integration: When using Signal with Bridge, it is possible to create a workflow that enables Signal to be run against local codebases, such as folders or Git project directories, and, when using Project mode, scan findings can be uploaded to a Black Duck platform for centralized visibility. Currently, Project mode supports integration with Polaris. For more details, see Using Bridge CLI with Signal.


===== TOPIC: Signal CLI =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id OHhk5dWIw9oUxRLShfedOw)

How to install, configure and run a standalone Signal scan from the command line and view results in a SARIF report.

Contents

Prerequisites

Install the binary

Configure the LLM connection

Run a scan

Review the results

Prerequisites

An API Key for the LLM that Signal will use.

A Signal Enterprise or Developer subscription.

For more information about available Signal flags, see Signal Reference Guide.

Install the binary

Follow the steps to scan your code with Signal CLI standalone:

Go to Signal CLI Binary to download and extract the file.

Rename the extracted executable to signal and move it to a directory on your PATH.

Move the executable to a directory on your PATH.Note: Linux or macOS: /usr/local/bin or ~/.local/bin

Windows: %LOCALAPPDATA%\Programs\Signal\

On Windows, add the folder to PATH through System Properties > Environment Variables

Verify that Signal is available on your PATH by running the command:signal --version

Configure the LLM connection

Signal requires an LLM endpoint URI and an API key. You can provide them using either of the following methods:Option A: Provide the values directly on the CLIsignal --llm-uri https://llm.core.blackduck.com \
--llm-key YOUR_API_KEY \
src

To avoid storing the key in your shell history, you can assign it to an environment variable:

Linux or macOS using Bash or Zshexport MY_LLM_KEY=YOUR_API_KEY

signal --llm-uri https://llm.core.blackduck.com \
  --llm-key "$MY_LLM_KEY" \
  src

Windows PowerShell$env:MY_LLM_KEY = "YOUR_API_KEY"

signal --llm-uri https://llm.core.blackduck.com `
  --llm-key $env:MY_LLM_KEY `
  src

Option B: Use a .signal configuration file

You can set the LLM key using the configuration file, but if the same setting appears in both the configuration file and the command line, the explicit CLI flag takes precedence.

Create a minimal .signal file in the root of your project:[SCAN]
llm_uri = https://llm.core.blackduck.com
llm_key = ${MY_LLM_KEY}
llm_model = claude-sonnet-4-6

Configuration-file values support ${VAR} interpolation from the environment, allowing you to keep the API key out of the file.

Verify the LLM credentials with the following code:signal src \
  --check-llm True \
  --llm-uri https://llm.core.blackduck.com \
  --llm-key YOUR_API_KEYThat way, Signal probes each configured LLM endpoint and exits before scanning.

For more details, see Signal config file.

Run a scan

After installing and configuring Signal, follow the steps to run a scan:

From the root of your project, point Signal at the directory you want to scan. Replace src with the path to your source code:signal --llm-uri https://llm.core.blackduck.com \
  --llm-key YOUR_API_KEY \
  src

Signal analyzes the files under src and writes its findings to results.sarif in the current working directory.Important: Signal overwrites results.sarif on each run.

The default model used for the scan is claude-sonnet-4-6. To select a different model, add the --llm-model option:signal --llm-model MODEL_NAME src

For per-agent model overrides, including --llm-model-agent and --llm-model-sca, and for all other available flags, see the Signal Reference Guide.

Review the results

To review the results, open results.sarif file in a SARIF-compatible viewer. Some examples you could use are:Visual Studio Code: Install the SARIF Viewer extension, and then open results.sarif.

Visual Studio: Open the file with the Microsoft SARIF Viewer extension.

GitHub code scanning: Upload the SARIF file through the code-scanning API or a GitHub Actions workflow.


===== TOPIC: Coding Assistants =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id fjduKYSb9H6pOuRf3HB48Q)

The Signal MCP Server facilitates the analysis of code from within a developer's coding assistant. The MCP server is distributed as an NPM package and is available from the public NPM registry via npx
        @black-duck/mcp-server@latest.

Contents
Environment Variables

Black Duck MCP configuration

Log location

IP Allowlist

Signal with coding assistants

Environment Variables
The Signal MCP server uses environment variables for its configuration. The following are the most commonly used when adding the Signal MCP server to a coding assistant. For the complete list of configuration options, see the Signal Reference Guide.

Variable

Default value

Description

BLACKDUCK_MCP_GATEWAY_URL
https://llm.core.blackduck.com/
LLM Gateway URL

BLACKDUCK_MCP_GATEWAY_KEY
No default value. 
LLM Gateway API Key for enhanced AI analysis

BLACKDUCK_MCP_LOG_LEVEL 
info
Signal Logging Level. Log level: error, warn, info, or debug

BLACKDUCK_HOME
User's home directory
Override the default .blackduck folder location

BLACKDUCK_MCP_TOOL_TIMEOUT
1800000 (30 min)
Scan timeout in milliseconds

Black Duck MCP configuration
You can set these variables in your MCP client configuration:

 {
  "servers": {
    "black-duck": {
      "type": "stdio",
      "command": "npx",
      "args": ["@black-duck/mcp-server@latest"],
      "env" : {
        "BLACKDUCK_MCP_GATEWAY_KEY": "YOUR_LLM_API_KEY",
        "BLACKDUCK_MCP_LOG_LEVEL": "info" 
    }
    }
  }
}

Log location
All MCP logs are written to /Users/<username>/.blackduck/mcp/logs/ for Linux/mac and C:\Users\<Username>\AppData\Roaming\BlackDuck\mcp\logs\ (customizable via BLACKDUCK_HOME):

black-duck-mcp.log - Combined log (all levels)

black-duck-mcp-error.log - Error-only log

IP Allowlist
The following URLs and IP addresses must be accessible for the MCP server to function properly:

URL
IP Address

repo.blackduck.com
34.149.5.115

llm.core.blackduck.com
104.18.36.253

Note: Ensure your firewall allows outbound HTTPS (port 443) connections to these endpoints.

Signal with coding assistants
Black Duck Signal can work with different AI coding assistants like Copilot to secure your code, including code generated by agentic workflows. Select your preferred coding assistant:

Signal and Claude Code

Signal and Codex CLI

Signal and Cursor

Signal and Gemini

Signal and JetBrains

Signal and Visual Studio with GitHub Copilot

Signal and VS Code with GitHub Copilot

Signal and Windsurf


===== TOPIC: Signal and Claude Code =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id ixkusxIoyIQQXA5nwicHGg)

How to register the Black Duck MCP server with Claude. 

Note: Available with: Signal Developer and Signal Enterprise.

Prerequisites:Node.js 24 or higher. If you need to download Node.js, see Node.js download. 

Claude Code. If you need to install Claude, see Claude Code - Quickstart.

A Signal Enterprise or Developer subscription.

Follow the steps to register Black Duck's MCP server for Claude Code: Install with CLI commands

$ claude mcp add black-duck --transport stdio --scope user --env BLACKDUCK_MCP_GATEWAY_KEY=YOUR_LLM_API_KEY -- npx @black-duck/mcp-server@latestAbout this codeblock:

This two-part instruction stores the MCP configuration in Claude’s system, then uses NPX to install and run the Black Duck MCP server and establish communication between the two. 

Be sure to substitute your API key environment variable after key=. 

Including --scope user sets the MCP at the user level and not system-wide. This prevents other users from accessing the MCP server with your credentials. 

 Verify your setup
Start Claude Code.

$ claude

 Ask Claude to scan some of your files using Black Duck.

Alternative installation methods

If this method didn't work for you, or you prefer a different method, see installing MCP servers.


===== TOPIC: Scan local files =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id 8a0GSNsRz1EeMdzh6FCNFA)

Bridge CLI can be used to run Signal to perform an AI assessment of local files or directories in a project, independent of Git history. The scanned files and folders can be controlled using include and optional exclude path lists. This task is for Bridge CLI users. For more details, see Bridge CLI Overview.

Prerequisites
Bridge CLI is installed and available on the system PATH.

Access to a project directory containing the files to scan.

A valid Signal LLM API key.

A Signal Enterprise or Developer subscription.

Follow the steps to run a local files scan:

Download the latest version of Bridge CLI, if you haven't installed it already. To download, see Bridge Binaries Download.

Add Bridge CLI to your $PATH variable.

Save a valid LLM API key in the BRIDGE_SIGNAL_LLM_KEY environment variable.

export BRIDGE_SIGNAL_LLM_KEY=<LLM_API_KEY>

Run the Bridge CLI Signal workflow at the root level of your project.

bridge-cli --stage signal \
  signal.mode=FILES \
  signal.include="src/main,src/dev,pom.xml" \
  signal.exclude="src/dev/resources/generated"Bridge will use the configuration to start Signal to perform an AI assessment of files and folders in the project directory. When the scan has completed, the following outputs will be provided:

A SARIF report file will be generated at .bridge/signal-controller/results.sarif within the current working directory where Bridge CLI was called from.

An exit code of 0 will be issued to signal success.

Signal CLI commands quick reference
The following parameters enable further customization. Use the related links information section to access the reference guide for the commands. For additional support, see Bridge Reference Guide.

CLI Argument
Description

project.directory
By default Black Duck Signal scans the files and folders in the current working directory. This behavior can be overridden by specifying the absolute path for the project.directory argument.

signal.version
By default Bridge downloads the latest version of Signal from the Black Duck repository. This behavior can be overridden by specifying a version string, e.g. 0.2.9.

signal.args
Specify additional arguments to be passed directly to Signal, e.g. "--dataflow true --log-level debug".


===== TOPIC: Scan uncommitted changes =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id XBRDb3XpMO6IjYIYjx2wZA)

Bridge CLI can be used to run Signal to perform a diff scan of uncommitted, tracked files in a Git project directory. This task is for Bridge CLI users. For more details, see Bridge CLI Overview.

Black Duck Signal provides the uncommitted scan mode to perform a diff scan of uncommitted tracked files. The Signal adapter configures Git diff-based analysis for the Git repository located at the project directory.

Prerequisites
The following prerequisites are required to run a diff scan:

Bridge CLI is installed and available on the system PATH.

Access to a Git project directory.

There are changes in uncommitted, tracked files.

A valid Signal LLM API key.

A Signal Enterprise or Developer subscription.

Follow the steps to run a diff scan:

Download the latest version of Bridge CLI, if you haven't installed it already. To download, see Bridge Binaries Download.

Add Bridge CLI to your $PATH variable.

Save a valid LLM API key in the BRIDGE_SIGNAL_LLM_KEY environment variable.

export BRIDGE_SIGNAL_LLM_KEY=<LLM_API_KEY>

Run the Bridge CLI Signal workflow at the root level of your project.

bridge-cli --stage signal \
  signal.mode=UNCOMMITTEDBridge will use the configuration to start Signal to perform a diff scan of uncommitted changes. When the scan has completed, the following outputs will be provided:

A SARIF report file will be generated at .bridge/signal-controller/results.sarif within the current working directory where Bridge CLI was called from.

An exit code of 0 will be issued to signal success.

Signal CLI commands quick reference
The following parameters enable further customization. Use the related links information section to access the reference guide for the commands. For additional support, see Bridge Reference Guide.

CLI Argument
Description

project.directory
By default Black Duck Signal scans the files and folders in the current working directory. This behavior can be overridden by specifying the absolute path for the project.directory argument.

signal.version
By default Bridge downloads the latest version of Signal from the Black Duck repository. This behavior can be overridden by specifying a version string, e.g. 0.2.9.

signal.args
Specify additional arguments to be passed directly to Signal, e.g. "--dataflow true --log-level debug".

signal.git.execution.path
By default Signal uses the Git binary accessible from the system PATH. This behavior can be overridden by specifying the absolute path to the Git binary using the signal.git.execution.path argument.


===== TOPIC: Signal's LLM Agents [BETA] =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id OuG~YeoACrFy1KVAN_MfRw)

Describes Signal's seven LLM agents, their roles in the analysis pipeline, and guidance for selecting models in a BYO-LLM configuration.

Contents

Overview

Quick reference

Recommended models for each agent

Mixed Provider Configurations

Overview
Signal uses 7 distinct LLM agents, splitting the LLM traffic into 5 chat agents (which consume a BaseChatModel client at runtime) and 2 embedding agents (which consume an Embeddings client). Every agent has its own precedence chain, so any agent can be overridden without affecting the others.

Since each agent serves a specific purpose in the analysis pipeline, they have very different performance characteristics — which is why you may want to assign different models, providers, or timeouts to each one.

Table 1. Agent

Purpose

Typical Workload

singlefilescan-agent
Single-file vulnerability detection; the primary security-analysis pass. Runs once per source file in the scan target.
Highest per-call token spend in the pipeline. Use your most capable reasoning model here.

dataflow-agent
Cross-file dataflow tracing; walks control flow through function calls, module boundaries, and class hierarchies.
Many small calls per target. Latency compounds because the agent chains decisions; use a fast reasoning model.

oversight-agent
False-positive triage and second-pass review. Runs both the initial triage prompt and the follow-up review prompt through one client.
Lower per-target volume than dataflow, but every finding runs through it before it reaches the SARIF report.

exploitation-agent
Exploit summaries and attack-chain narrative. Runs per-finding to produce the human-readable exploitation description.
Similar to dataflow and oversight; typically shares their model choice.

sca-agent
Software composition analysis; supervisor and sub-agents for dependency and CVE reasoning.
Volume depends on the dependency graph. Requires reliable tool-calling; a solid mid-tier model handles this well.

mergekey-embed-agent
Vector embeddings for merge keys; the mechanism that links a finding across successive scans so it stays trackable when files are renamed or line numbers shift.
Embedding calls only. Requires an embedding model such as text-embedding-3-large, text-embedding-005 (GCP), or amazon.titan-embed-text-v2:0 (Bedrock).

oversight-embed-agent
Vector embeddings for oversight-rule text; matches findings against the built-in vulnerability classification rules via cosine similarity.
Embedding calls only. Can safely use a cheaper embedding model than mergekey-embed since the strings are shorter and the accuracy bar is lower.

Quick reference
The table below shows the recommended default model and the key capability requirement for each agent. For a full explanation of what each requirement means and how to diagnose failures, see Agent Capability Requirements [BETA].

Table 2. Agent

Purpose

Recommended default

Key requirement

singlefilescan-agent
Per-file vulnerability detection
claude-sonnet-4-6
Frontier reasoning; large context window

dataflow-agent
Cross-file taint tracing via React and file tools
o3-mini
Native tool-calling; strict structured output

oversight-agent
False-positive triage and rule review
o3-mini
Native tool-calling; strict structured output

exploitation-agent
Executive summary, zero-day list and attack chain
o3-mini
Long-context reasoning; strict structured output

sca-agent
Python SCA (supervisor + 
gpt-4o
Native tool-calling; JSON tool arguments

mergekey-embed-agent
Finding-linking embeddings
text-embedding-3-large
≥ 1024-dim embedding; stable across runs

oversight-embed-agent
Rule-taxonomy cosine matching
text-embedding-3-small
≥ 512-dim embedding model

Recommended models for each agent
Your most capable reasoning model — singlefilescan-agent

The singlefilescan-agent is the primary vulnerability-detection engine: every source file in the scan target is analysed once through this client. Its dominant cost concern is reasoning depth; a model that misses subtle injection paths or skips entire control flows produces false negatives, and false negatives in security analysis are the most expensive kind of error because they are invisible.

Recommended models: Claude Sonnet 4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, o3-mini.

Deviation case: On small targets where total LLM spend is already low, a smaller model keeps iteration fast during config tuning — but switch back to a top-tier model before relying on the results.

Symptom of under-provisioning: Findings volume drops without a corresponding decrease in target complexity, or --check-llm passes but real scans return suspiciously empty result sets.

Table 3. singlefilescan-agent: recommended models by providerProvider

Recommended

OpenAI
gpt-4o, gpt-4.1

Anthropic direct
claude-sonnet-4-6, claude-opus-4-6

Azure OpenAI
gpt-4o or gpt-4.1 deployments

Azure AI Anthropic
claude-sonnet-4-6

AWS Bedrock Anthropic
anthropic.claude-sonnet-4-6, anthropic.claude-opus-4-6

GCP Vertex Gemini
gemini-2.5-pro

Smaller reasoning models — dataflow, oversight, and exploitation agents

These three agents run after the singlefilescan pass, mostly per-finding, and consume far fewer tokens per call. Latency matters more here than peak reasoning depth; every agent makes many small decisions in series, and a slow model multiplies wait time.

Recommended models: Claude Sonnet 4, Gemini 2.5 Pro, o3-mini, o4-mini, o3, o1.

Deviation case: If your codebase pushes oversight or dataflow into territory a smaller model handles poorly (deeply nested call graphs, large polyglot dataflow), you can run the same model as your singlefilescan-agent across all three. The cost premium is bounded because their combined volume is a fraction of singlefilescan.

Symptom of under-provisioning: Oversight false-positive rate climbs, dataflow agent gives up early or loops without converging, exploitation summaries read as generic boilerplate.

Table 4. dataflow, oversight, and exploitation agents: recommended models by providerProvider

Recommended

OpenAI
o3-mini, o4-mini, o3, o1

Anthropic direct
claude-sonnet-4-6, claude-opus-4-6

Azure OpenAI
o3-mini, gpt-4o deployments

Azure AI Anthropic
claude-sonnet-4-6

AWS Bedrock Anthropic
anthropic.claude-sonnet-4-6, anthropic.claude-opus-4-6

GCP Vertex Gemini
gemini-2.5-pro

Midrange reasoning model — sca-agent

The sca-agent uses a supervisor pattern where the model's job is dispatch — delegating to a pip-audit sub-agent and a knowledge-base sub-agent — rather than deep analysis. Frontier reasoning is not required here; a reliable mid-tier model with real tool-calling handles it well.

Recommended models: GPT-4o, GPT-4.1, Claude Sonnet 4, Gemini 2.5 Pro or Flash.

Symptom of under-provisioning: The supervisor stops delegating (produces plain text output instead of tool calls); pip-audit is not invoked.

Table 5. sca-agent: recommended models by providerProvider

Recommended

OpenAI
gpt-4o, gpt-4.1

Anthropic direct
claude-sonnet-4-6

Azure OpenAI
gpt-4o deployment

Azure AI Anthropic
claude-sonnet-4-6

AWS Bedrock Anthropic
anthropic.claude-sonnet-4-6

GCP Vertex Gemini
gemini-2.5-pro, gemini-2.5-flash acceptable

The embedding agents

The mergekey-embed-agent and oversight-embed-agent produce vector embeddings, not text completions — the model lists are completely separate from the chat agents. Both benefit from high-dimensional embeddings (better semantic separation), but mergekey-embed-agent in particular needs embeddings stable across runs: merge keys link findings between successive scans, so switching embedding models mid-project causes findings to appear new even when the underlying issue has not changed.

Recommended models: text-embedding-3-large / text-embedding-3-small (OpenAI-compatible), text-embedding-005 (GCP Vertex), amazon.titan-embed-text-v2:0 (Bedrock).

Deviation case: The oversight-embed agent operates on shorter strings (classification rules) than mergekey-embed does (finding summaries), so a cheaper embedding model is acceptable for oversight-embed without meaningfully affecting accuracy. Signal's managed-mode defaults already split them this way.

Symptom of under-provisioning: Merge keys churn between scans (existing findings appear as new ones), or oversight classification accuracy drops sharply on borderline rules.

Table 6. Embedding agents: recommended models by providerProvider

Recommended (mergekey-embed / oversight-embed)

OpenAI
text-embedding-3-large / text-embedding-3-small

Azure OpenAI
text-embedding-3-large deployment

AWS Bedrock
amazon.titan-embed-text-v2:0, cohere.embed-multilingual-v3

GCP Vertex
text-embedding-005, gemini-embedding-001

Mixed Provider Configurations
Signal supports mixing different providers within the same scan, enabling different providers and models to be used for different agents. Each agent serves a specific purpose in the analysis pipeline, and they have very different performance characteristics — which is why enabling models from different providers can have many benefits, including:

Cost optimisation: The singlefilescan-agent processes every source file and dominates LLM spend. You might use a cost-effective model on one provider for singlefilescan while using a premium model on another provider for the four lighter chat agents where reasoning quality matters most, or vice versa.

Capability matching: Embedding models and chat models have different strengths. OpenAI's text-embedding-3-large may outperform alternatives for embeddings, while Anthropic Claude or Google Gemini may be preferred for code analysis.

Infrastructure constraints: Your organisation may have separate contracts, quotas, or network paths for different cloud providers.

Gradual migration: When moving from one provider to another, you can switch one agent at a time and validate results before completing the transition.


===== TOPIC: Agent Capability Requirements [BETA] =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id Km58~tIfMxAVPGSsIikLig)

Describes the structured-output, tool-calling, and context-window requirements each Signal agent places on its configured model, with failure symptoms and provider-specific notes to help you diagnose scan issues.

Contents

Capability vocabulary

Per-agent requirements and failure modes

Provider-specific notes

Models not recommended for Signal agents

Capability vocabulary

      
      The per-agent requirements below reference four capability axes. If you are evaluating a
        model that is not listed in the Recommended
          models tables, check it against these first.

      Structured-output mode

      How the response schema is enforced on the wire:

      OpenAI JSON object mode. The request instructs the model to produce a JSON
          object, but the shape is not validated server-side. The most permissive mode; most
          OpenAI-compatible servers honor it. Signal uses this
          mode for the singlefilescan-agent.

OpenAI JSON schema mode. The request includes the full expected schema and the
          server validates output against it. Reliable on OpenAI (o-series,
          gpt-4o), Azure OpenAI, and a subset of high-end hosted gateways.
            Silently ignored by most local inference servers (Ollama, llama.cpp, vLLM) — the
          model generates freely and often wraps output in markdown code fences, which Signal's parser rejects immediately.

Anthropic tool-use (function calling). The schema is bound as a synthetic tool
          and the model is forced to "call" it. Signal
          automatically routes Claude models. Reliable on Anthropic direct, Azure AI Services
          Anthropic, and AWS Bedrock Anthropic.

Dense vector. Embeddings only. The sole requirement is fixed-dimension
          output.

      Reasoning tier

      Frontier: GPT-4o / o-series, Claude Sonnet 4.x / Opus 4.x, Gemini 2.5 Pro.
          Reliable on multi-step reasoning under a schema constraint.

Midrange: GPT-4o-mini, Claude Haiku 4.x, Gemini 2.5 Flash. Suitable for
          tool-orchestration agents where the model's job is dispatch rather than deep
          analysis.

Small: Any model roughly 13 B parameters or smaller, including typical 4–8
          B-class open models. Not recommended for any Signal
          agent that enforces structured output; see Models not recommended for Signal agents.

      Tool-calling

      Required for the dataflow-agent, oversight-agent (via schema-as-tool binding), exploitation-agent, and sca-agent. The model must implement OpenAI-compatible tools / tool_calls or Anthropic tool-use natively. This is not the same as "can produce JSON": a model can be a reliable JSON generator and still fail to handle tool calls correctly. Many local models fall in exactly that gap.

      Context window

      A context window of 128k tokens or larger is recommended for the singlefilescan-agent, dataflow-agent, and exploitation-agent. The singlefilescan agent sends entire source files; the dataflow agent accumulates tool-call history across multiple steps; the exploitation agent receives the top findings with their full source context. A minimum of 32k tokens is a hard floor for any agent.

    

Per-agent requirements and failure modes

      

      singlefilescan-agent

      Uses JSON object mode, the most forgiving structured-output method Signal employs. Tool-calling is not required; each invocation is
        a single-shot prompt. Runs once per source file, so it dominates total LLM spend on large
        repositories.

      Failure symptoms with underpowered models: Even midrange models generally return parseable output for this agent, but classification quality degrades visibly — missed vulnerability classes, incorrect rule IDs, inaccurate line ranges. If you notice degraded output quality without errors, upgrade the tier before investigating other agents.

      dataflow-agent

      Uses JSON schema mode with tool-calling. The agent iteratively calls file-inspection tools to trace taint flows across files, then produces a structured finding result. Signal automatically uses the tool-use (function-calling) path for Claude models; JSON schema mode for all others. Runs concurrently across findings, bounded by the --agent-limit setting (default 10).

      Failure symptoms: All three are logged as FAIL dataflow/<file> (guid=…) after 5 attempts:

      Validation Error. The model returns markdown-fenced output (for example,
            ```json … ```) instead of a raw JSON object. Root cause: the model or
          local gateway silently ignored the JSON schema requirement. Retries will not help; switch
          to a model with reliable structured output.

Silent tool-call failures. The model emits tool calls in an unexpected format;
          they are dropped silently, and the agent loop stalls. Look for empty AI messages in the
          debug output.

Schema mismatch. The model returns valid JSON with the wrong shape: missing
          fields, wrong value types, or incorrect field names. Almost always means the model is too
          small for the schema complexity. Upgrade to a frontier-tier model.

      oversight-agent

      Runs two prompts through one client: a triage pass that re-labels obvious false positives, and a review pass that optionally augments the model with the top-3 cosine-similar rules from the built-in rule taxonomy (when oversight_embedding_enabled=true). Uses the same structured-output and tool-calling requirements as the dataflow agent.

      Failure symptoms: Same as dataflow. Additionally: if the oversight pass is not re-labeling any findings as false positives, the model may be consistently agreeing with initial scan labels regardless of evidence — a behavior failure rather than a hard error. This is common with midrange models on complex codebases. Upgrade the tier.

      exploitation-agent

      Single-shot prompt against a large input — the top scan findings, each with source context. Only runs when --summary is enabled. Uses JSON schema mode / tool-use; tool-calling is not required. Context window matters more here than for the other chat agents because the full finding set is sent in one prompt.

      Failure symptoms: Truncated summaries (context window too small for the input); flat, non-specific attack chains (model cannot reason across multiple findings); hallucinated CVE numbers.

      sca-agent

      LangGraph supervisor pattern: the main agent delegates to a pip-audit sub-agent and a knowledge-base sub-agent. Tool-calling is the agent's primary mechanism — its job is dispatch, not deep analysis, so a reliable mid-tier model with real function-calling is sufficient. Runs independently of the SAST pipeline alongside other agents.

      Failure symptoms: The supervisor stops delegating (single-model text output instead of tool calls); pip-audit invocation missing from the agent trace. Both indicate the model is not handling tool dispatch correctly.

      mergekey-embed-agent

      Produces dense vector embeddings for finding text so that Signal can link findings across successive scans by cosine similarity. Any embedding model with ≥ 1 024 dimensions works. Dimension is not enforced by Signal itself — but switching embedding models mid-project invalidates the finding-linking index, causing existing findings to appear new every scan even when the underlying issue has not changed. Do not change the embedding model once a project is in active use.

      oversight-embed-agent

      Embeds the built-in rule taxonomy and finding descriptions for cosine-similarity matching, then feeds the top-3 matches to the oversight review prompt. Only active when oversight_embedding_enabled=true. A smaller, cheaper embedding model is acceptable here (default is text-embedding-3-small) because the rule taxonomy strings are short and the top-3 selection is not sensitive to embedding quality above a baseline.

    

Provider-specific notes

      
      
          AWS Bedrock (Anthropic). Signal enables prompt caching by default (llm_prompt_caching=true). Cache-write incurs a small premium on the first request; every subsequent request within the cache TTL bills at approximately 10% of the base rate. This is a free performance and cost win — do not disable it unless you have a specific reason to.

        

          Azure AI Services Anthropic (*.cognitiveservices.azure.com, *.services.ai.azure.com with a Claude model). The Azure proxy rejects "assistant message prefill" — a technique some prompt patterns use. Signal automatically works around this restriction; no operator action is needed. If you see HTTP 400 errors stating "conversation must end with user role," your version of Signal predates this fix; upgrade to the current release.

        

          Azure OpenAI (*.openai.azure.com). An explicit api_version value is required in your configuration (for example, 2024-12-01-preview). A missing api_version raises SIGNAL-E117 at startup. This applies only to the Azure OpenAI endpoint; Azure AI Services routes through the Anthropic path and ignores api_version.

        

          OpenAI o-series (o1, o3, o4 and prefixed variants). These models reject the temperature parameter with HTTP 400. Signal handles this automatically; no operator action is needed.

        

          GCP Vertex Gemini. Uses the native Vertex API, not an OpenAI-compatible endpoint. Requires gcp_project, gcp_region, and a service-account key in your configuration. Structured output uses Vertex's own JSON mode, which behaves similarly to JSON schema mode in its strictness.

        

          Local OpenAI-compatible gateways (Ollama, llama.cpp, vLLM, LM Studio). These servers typically accept any response_format field and silently ignore anything they do not understand. See Models not recommended for Signal agents.

        

    

Models not recommended for Signal agents

      
      Small local models — such as Gemma 2/3/4, Llama-3-8B, Mistral-7B, and similarly-sized quantized models served through Ollama, llama.cpp, vLLM, or LM Studio — are not supported for Signal's ReAct agents (dataflow-agent, oversight-agent, exploitation-agent, sca-agent).

      These models fail every structured-output requirement that the dataflow and oversight agents enforce:

      They do not honor the JSON schema requirement — the local server forwards the request, but the model does not understand it and generates freely, often wrapped in markdown code fences that Signal's parser immediately rejects.

Their tool-calling implementations are typically incomplete — tool calls come out malformed or as free-form text, causing the agent loop to stall without converging.

Their context windows are too small for real dataflow traces, which accumulate tool-call history across multiple steps and can grow large on non-trivial codebases.

      What might work: pointing only the singlefilescan-agent at a small local model (using --llm-singlefilescan-agent-model) is sometimes viable, because that agent uses the more forgiving JSON object mode. However, you lose all cross-file verification, all false-positive triage, and the executive summary — a significant reduction in scan capability.

      If you must experiment with local models: configure only the singlefilescan-agent to use the local model and keep a frontier model on every other agent. Signal's per-agent configuration surface makes this straightforward — see BYOLLM configuration from the CLI [BETA]. Treat any findings that do not survive frontier-model dataflow verification as first-pass triage only, not as production results.


===== TOPIC: BYOLLM [BETA] =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id YUNO2lj47cRmGK1ZaaD75w)

Bring Your Own Large Language Model (BYOLLM) allows customers to connect Signal to their own Large Language Model (LLM) endpoints instead of using the managed Signal LLM service.

Signal performs software static analysis using an LLM-based approach, where all LLM interactions go through the Black Duck gateway. However, when customers enable BYOLLM, they are able to point Signal to a supported LLM provider of their choice, so all AI-powered analysis runs against the infrastructure they control, which is particularly interesting for customers with strict data residency requirements, existing enterprise LLM agreements, or cost optimization goals.

Benefits of enabling BYOLLM
Data sovereignty: Keep source code and analysis prompts within their own cloud tenancy or on-premises network; nothing leaves your perimeter.​

Cost control: Use existing enterprise LLM contracts, reserved capacity, or volume discounts instead of additional spend.​

Model preference: Choose specific model versions (e.g., GPT-4o, Claude Sonnet, Gemini 2.5 Pro) that match their accuracy or latency requirements.

Air-gapped environments: Run Signal in networks with no outbound internet access by pointing at an internal LLM proxy.​

Compliance: Satisfy regulatory requirements that prohibit sending data to third-party AI services.

Auth support in V1: Static API keys or Bearer tokens for URI-based providers (OpenAI, LiteLLM, Azure), GCP service-account JSON keys with auto-refreshed OAuth2 for Vertex AI, and IAM service-specific Bearer credentials for AWS Bedrock.

Auth support in V1
Static API keys or Bearer tokens for URI-based providers, such as OpenAI, LiteLLM and Azure.

GCP service-account JSON keys with auto-refreshed OAuth2 for Vertex AI.

IAM service-specific Bearer credentials for AWS Bedrock.


===== TOPIC: Preflight validation [BETA] =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id 4uJU~WyShorEC8fjQO1Z5g)

A full Signal scan can take tens of minutes on a large target, so discovering halfway through that one of your seven LLM agents is misconfigured; bad URL, expired key, missing model deployment, wrong API version; is an expensive failure. The --check-llm flag exists to surface that class of failure in seconds, before a single source file is scanned.

What --check-llm actually does

When you pass --check-llm True, Signal skips the scan entirely and instead walks every agent you have configured, instantiates the same client class that a real scan would use, and runs a minimal probe against the live endpoint:

Chat agents (singlefilescan, dataflow, oversight, exploitation, sca); issues an invoke("Hello") completion to verify that the URL resolves, the key authenticates, the model exists on the endpoint, and (for Azure OpenAI) the api_version is acceptable.

Embedding agents (mergekey-embed, oversight-embed); issues an embed_query for the fixed string "test" and verifies the returned vector has non-zero dimensionality.

Each agent's result is reported with its endpoint, model name, provider, latency, and (on failure) the agent-tagged error message; the same message you would see if the same problem surfaced mid-scan, so debugging the preflight failure is identical to debugging the real one.

Use cases

First-time setup — run it once after writing your initial .signal file or assembling your CLI invocation. Almost every "BYOLLM doesn't work" issue customers report is caught by preflight.

After credential rotation — Bedrock service-specific credentials, Azure keys, GCP service-account keys all change. Run --check-llm after every rotation to confirm the new credential reaches every agent before triggering a real scan.

In CI, before queueing a scan — exit code 0 means every configured agent is reachable. Exit code 1 means at least one agent failed; fail your pipeline early instead of consuming scan budget.

As a smoke test after upgrading Signal — provider integrations occasionally shift between releases (model deprecations, API version requirements changing). Preflight catches the regression cheaply.

Output modes

The default human-readable output is a Rich table. For machine consumption, pass --check-llm-json True (which implies --check-llm
				True) and Signal emits a single JSON document on stdout; no other noise; The JSON schema is versioned (schema_version: "1") and is the stable contract these tools rely on; field additions are non-breaking, removals or type changes bump the version. The test_check_llm_json_e2e.py integration suite regression-tests the schema, so the JSON shape will not drift silently between releases.

Valid Configuration output example

                                LLM Endpoint Validation
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Agent                 ┃ Endpoint                     ┃ Model                    ┃ Status                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ singlefilescan-agent  │ GCP Vertex AI                │ gemini-2.5-pro           │ ✅ OK                  │
│ dataflow-agent        │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ oversight-agent       │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ exploitation-agent    │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ sca-agent             │ https://litellm.example/v1   │ gpt-4o                   │ ✅ OK                  │
│ mergekey-embed-agent  │ https://litellm.example/v1   │ text-embedding-3-large   │ ✅ OK (dim=3072)       │
│ oversight-embed-agent │ https://litellm.example/v1   │ text-embedding-3-small   │ ✅ OK (dim=1536)       │
└───────────────────────┴──────────────────────────────┴──────────────────────────┴────────────────────────┘

All LLM endpoints validated successfully.

Invalid Configuration output example

A failed agent shows ✗ FAIL: E<code>: <message> in the Status column with the message truncated to 80 characters. The same information appears in the JSON output under agents[].error_code and agents[].error_message with no truncation.

                                                                                          LLM Endpoint Validation                                                                                           
┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Agent                 ┃ Endpoint                                               ┃ Model                  ┃ Status                                                                                         ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ singlefilescan-agent  │ https://llm.labs.blackduck.com/v1/                     │ claude-sonnet-4        │ ✗ FAIL: E110: Error code: 401 - {'error': {'message': 'Authentication Error, Invalid proxy ser │
│ dataflow-agent        │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ oversight-agent       │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ exploitation-agent    │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ sca-agent             │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ o3-mini                │ ✅ OK                                                                                          │
│ mergekey-embed-agent  │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ text-embedding-3-large │ ✅ OK (dim=3072)                                                                               │
│ oversight-embed-agent │ https://oai-llm-gw-client-byo-signal.openai.azure.com/ │ text-embedding-3-small │ ✅ OK (dim=1536)                                                                               │
└───────────────────────┴────────────────────────────────────────────────────────┴────────────────────────┴────────────────────────────────────────────────────────────────────────────────────────────────┘


===== TOPIC: AI security, data protection, and trust =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id SeKsRfoJBm40f_Zq4N3HQw)

Black Duck Signal is designed as a responsible, human-centered AI security analysis platform, with strong controls around LLM access, data isolation, and enterprise compliance.

This topic describes the security posture, data handling practices, and large language model (LLM) usage for Black Duck Signal, addressing common customer questions around AI trust, privacy, and compliance.

LLM models used
Signal AI Scanner uses large language models exclusively through the Black Duck–managed LLM Gateway. LLM selection, access, and orchestration are managed entirely by Black Duck.

Signal is designed with a model-agnostic architecture, and Black Duck currently uses and validates integrations with publicly available foundational models, including:

Anthropic (Claude)

OpenAI (GPT series)

Google Cloud AI (Vertex AI)

Azure OpenAI Service

Commercial LLMs and model training
The models accessed through the Black Duck LLM Gateway are public, commercial foundational models.

Black Duck does not:

Apply proprietary fine-tuning

Train or retrain models using customer data or source code

Use customer inputs to improve or modify model behavior

Customer data is used only at inference time to generate security findings.

LLM access architecture
Signal uses Black Duck's managed LLM gateway to perform AI-based scans.

Signal does not use customer-hosted LLM infrastructure

Signal does not require customers to connect their own LLM accounts

All LLM access is orchestrated, secured, and audited by Black Duck

This centralized approach ensures consistent security controls, monitoring, and governance across all customers.

Hosting locations
Signal uses Black Duck LLM infrastructure when performing scans. Customers do not provide or manage LLM infrastructure.

The validated LLM providers used by Black Duck operate on US-based infrastructure, including:

Anthropic: US-based infrastructure

OpenAI: US-based infrastructure

Google Cloud AI: US-based infrastructure

Azure OpenAI Service: US-based infrastructure

Black Duck centrally manages security controls, access policies, and auditing for all LLM interactions.

Human-in-the-loop safeguards
Signal is designed as a human-supervised analysis tool, not an autonomous decision-maker.

LLMs generate analytical findings and recommendations only

Signal does not directly modify customer code

At most, Signal may create merge requests requiring explicit human approval

Developers retain full authority to accept, modify, or reject recommendations

All findings require human judgment before any corrective action is taken.

Data privacy and isolation
Signal enforces strong data isolation and multi-tenancy controls:

Isolation enforced at the LLM provider API level

Per-organization authentication, authorization, and rate limiting

No cross-customer data sharing or visibility

Black Duck does not access or reuse customer source code across tenants

Each organization's usage and credentials remain fully isolated.

Monitoring, auditing, and logging
Signal implements comprehensive monitoring and observability for AI usage:

API call logging (timestamps, model used, token usage, latency)

Error tracking for failed scans and model timeouts

Usage metrics per customer, including performance and cost indicators

Audit trails covering scan requests, outputs, and user interactions

Eligibility for human review of high-risk or anomalous results

To balance scale, performance, and data minimization, full prompt and response content is not logged at scale. Sampling-based logging may be introduced for high-risk findings.

Training, updates, and model evolution
Black Duck does not train or fine-tune any LLMs used by Signal.

Foundational model updates occur per each provider's release schedule

Black Duck-owned updates focus on prompt engineering, orchestration logic, and scanning heuristics

Improvements are driven by security research, user feedback, and real-world testing

Model evolution is independent of customer data

Compliance and responsible AI practices
Signal is designed to support enterprise compliance and governance requirements:

Inference-only model usage (no training on customer or personal data)

Data Processing Agreements (DPAs) in place with supported LLM providers

Customer data retention and deletion policies enforced

Transparency that findings are generated using LLMs

All recommendations are user-overridable

HIPAA notice: Signal AI Scanner is not intended for processing HIPAA-regulated patient data in the current release, and no HIPAA compliance claims are made at this time.

Security certifications: Black Duck maintains SOC 2 Type II certification. Supported LLM providers offer their own enterprise security and compliance reports.


===== TOPIC: Signal FAQ =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id adLfX1KuRGF8aOKdT8kkBg)

Frequently asked questions about Black Duck Signal, including general product questions, LLM usage, and source code privacy.

Contents
General

Large Language Models (LLMs) Usage

Source Code Privacy

General
Q: What is Signal?

Black Duck Signal is an agentic application security solution that uses the power of LLMs to automatically find, prioritize, and fix security and other defects in source code, binaries, supply chain components, and running applications. Signal augments and refines AI analysis with context from Black Duck ContextAI™ containing over 20 years of human expert vetted knowledge, including insecure coding patterns; open source components, vulnerabilities, and licenses; and secure coding standards and best practices. With Signal, development and security teams get deep AI analysis of software risks without the noise, hallucinations, and inconsistencies found in solutions that do not have this context.

Q: What problem does this solve?

Fundamentally, Signal is designed to use AI to address the central problem with traditional application security tools. They generate too much "noise" in the form of large volumes of false-positive and low-value findings that require considerable human effort — both from developers and security analysts — to triage and prioritize. To compensate for this, teams often need to apply additional technologies, such as ASPM, cloud security integrations, and reachability analysis.

Signal takes a different approach to eliminate noise before it can be generated. By leveraging the intuitive nature of AI, Signal dramatically reduces security findings to those that are real and high priority to fix.

In the near term, Signal focuses on addressing four key customer needs:

Developers want to quickly find issues in code they just wrote or generated.

Developers are adopting AI-coding assistants and want code generation, testing, and defect fixing to all happen through those interfaces.

Security teams want to focus their efforts on the highest-risk security issues in the software they deliver.

Security teams waste a lot of time manually reviewing code in languages not supported by traditional SAST solutions.

Q: How is this different from asking a code assistant to analyze the code?

From a user perspective there is little to no difference between asking a coding assistant like Copilot or Claude versus asking Signal. In fact, by registering Signal with these coding assistants via MCP, the user simply asks the assistant to scan their code, and the request is directed to Signal by the coding assistant itself.

The key difference is in the fidelity of the findings. In our tests, Signal produced significantly better findings than general-purpose AI coding assistants.

Q: Is this replacing Coverity?

No. AI complements traditional static analysis solutions like Coverity and Polaris fAST Static by providing:

Support for languages for which static analysis rulesets are not available.

Better real-time analysis and code fixing in developer workflows.

Identification of security defects that rule-based analysis misses.

Q: What are the key features and benefits?

Signal addresses the four key customer needs with:

Real-time incremental analysis of new and modified code. Signal's context-aware AI analysis delivers accurate findings without the need to perform a full application scan.

Direct integration into AI-coding assistants via agent and Model Context Protocol (MCP) interfaces.

AI insights and context that complement traditional AST by identifying issues — including those often missed by rules engines — most likely to be exploited.

Universal language support. Signal's AI-based analysis is language-agnostic and able to analyze code in any modern or legacy programming language.

Q: Is the Black Duck knowledge base used for Signal agents?

The knowledge base used for Signal is branded as Black Duck ContextAI™. It combines the OSS component and BDSA information from the KnowledgeBase™ used by Black Duck SCA, as well as other security data and rules used by our SAST and SCA engines, analytics from our SaaS offerings, and best practices from our security consulting.

The initial code analysis use case at launch makes use of issue taxonomy information derived from Coverity. As Signal is expanded to cover other use cases, additional information from Black Duck ContextAI™ will be leveraged.

Large Language Models (LLMs) Usage
Q: Do you have a list of LLMs used that can be shared with customers?

Black Duck currently provides the LLM infrastructure. In the future, customers will be able to provide their own LLMs. We will provide a list of supported LLMs at that time.

Q: Where are the LLMs hosted?

We use a combination of LLMs hosted in Azure, AWS, and GCP.

Source Code Privacy
Q: Where is my source code going?

Signal programmatically crawls targeted source code on the user's system and sends individual files and excerpts to LLMs for analysis.

Note: Users will also have the option to point Signal to their own LLMs in the future. This is not available today.

Q: Is my source code stored or cached anywhere?

No caching occurs on the Black Duck side.

Q: Does Signal use my code for training LLM models?

No, Signal does not use customer code for training LLM models.

Q: Does Signal modify my source code?

Signal does not modify source code. If using Signal Developer within the IDE, coding assistants can interface with Signal to identify vulnerabilities and suggested fixes, but the application of those fixes is handled by the developer and coding assistant.


===== TOPIC: Signal release notes =====
# URL: https://docs.blackduck.com/r/blackduck-signal/latest/ (topic id 4RKMpkO6EtmpgrOkKE9r0Q)

September 2026
Bug fixes and technical improvements.

Speed and efficiency improvements.

New user guides to describing how to use Signal CLI and Signal with coding assistants. For more details, see Get Started with Black Duck Signal.

Bring Your Own LLM (BYOLLM) v1. When customers enable BYOLLM, they are able to point Signal to a supported LLM provider of their choice, so all AI-powered analysis runs against the infrastructure they control, which is particularly interesting for customers with strict data residency requirements, existing enterprise LLM agreements, or cost optimization goals. The BYOLLM feature is optional and existing configurations are unaffected. For more details, see BYOLLM [BETA].

Prioritization with Preview Report. Unordered results are now set into a ranked, filterable, self-describing actionability surface, severity ranking, novelty (detectableBy), exploitability (CISA KEV), a documented property contract, and a standalone HTML preview.

Connect a synthesis agent to Pockit. Signal's synthesis agent identifies multi step vulnerability chains across your codebase and surfaces the single most dangerous attack path after dataflow analysis. PoCKit exploit validation then actively attempts to confirm whether top ranked findings are exploitable, automatically removing false positives and providing full exploit evidence for confirmed threats. Both features are experimental and require --dataflow True; PoCKit additionally requires --synthesis True.

Crypto analysis is now enabled by default, improving the detection of both classical and post-quantum cryptography vulnerabilities.

July 2026
Bug fixes and technical improvements.

Improved 429 error handling with exponential backoff. Previously, when the LLM gateway returned a 429 error code requesting a retry, all retry attempts were made in rapid succession, causing them to fail and preventing the file from being processed correctly. Retry attempts are now spaced using exponential backoff, improving reliability when rate limits are encountered.

Pre-scan cost estimator for large codebases. When a scan targets a codebase larger than a configurable file-count threshold (default: 500 files), Signal runs a pre-scan estimator before starting the actual scan. This gives the user a low/mid/high range for input tokens, output tokens, and a wall-clock curation before the user commits to a potentially expensive run. The estimate is printed to the log along with language composition and enabled stages, then the user is prompted to confirm before the scan proceeds. Non-interactive environments auto-proceed after logging the estimate. If any sampled single-file-analysis calls were served from the LLM cache from a prior run, the projected numbers are not able to reflect the true cost. The estimator detects this and prints a warning.

Updated default SFA model. Signal now supports Claude Sonnet 4.6, and this is now the default model used for single file analysis.

Console progress update for the dataflow agent. Added progress logging in the dataflow and oversight agents so the users can see real-time status while the dataflow agent is running.

Enhanced cryptography analysis. Reviewed and improved the cryptography detection prompt, including evaluation of Post-Quantum Cryptography (PQC) handling and oversight agent coverage for crypto-related findings.

Crash recovery for Dataflow Agent. Signal periodically writes a checkpoint file during the expensive dataflow agent phase. On restart, previously completed tasks are skipped and only the remaining work is considered. The results are merged before handing off to oversight.

Auto-export SFA results. For scans exceeding 500 dataflow tasks, Signal automatically writes 2 hidden dot-files that appear and disappear in the same directory as --report-file: .{report_file}.sfa.json (interim SFA report file) and .{report_file}.df_checkpoint (checkpoint file). Both files are removed when the scan completes successfully. High disk usage is expected and will be optimized in subsequent releases. 

May 2026
New documentation covers Signal's AI security, data protection, and trust posture, including LLM architecture, data isolation, and compliance certifications.

April 2026
Black Duck Signal was released for general availability. Capabilities include the following:

Signal Developer: Scan your changes through the Black Duck MCP, an IDE or Bridge CLI.

Signal Enterprise: Scan an entire project in your pipeline to generate a SARIF report for Polaris or any platform that supports SARIF.

See the FAQ here.

Read the overview in documentation.
