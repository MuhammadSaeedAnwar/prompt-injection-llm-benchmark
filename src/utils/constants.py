"""Constants for benchmark."""

# Attack Categories
ATTACK_CATEGORIES = {
    "Direct": "Direct injection attacks embed malicious instructions in user prompts",
    "Indirect": "Indirect injection manipulates external data sources",
    "Jailbreak": "Jailbreak attacks use social engineering and roleplay",
    "Multi-Turn": "Multi-turn attacks exploit context accumulation over conversation turns",
    "Encoding": "Encoding-based attacks use obfuscation techniques",
}

DIRECT_SUBCATEGORIES = [
    "Instruction Negation",
    "Priority Escalation",
    "Delimiter Confusion",
]

INDIRECT_SUBCATEGORIES = [
    "Document Poisoning",
    "Email Injection",
    "Cross-Document Propagation",
]

JAILBREAK_SUBCATEGORIES = [
    "Fictional Scenario",
    "Character Assumption",
    "Translation Bypass",
    "Code Generation Proxy",
]

MULTI_TURN_SUBCATEGORIES = [
    "Context Accumulation",
    "Incremental Escalation",
    "Memory Exploitation",
]

ENCODING_SUBCATEGORIES = [
    "Base64",
    "Unicode Homoglyph",
    "Markdown Injection",
    "ASCII Art",
]

# Complexity Levels
COMPLEXITY_LEVELS = ["Simple", "Intermediate", "Advanced"]

# Languages
LANGUAGES = [
    "English",
    "Mandarin Chinese",
    "Spanish",
    "French",
    "Arabic",
    "German",
    "Japanese",
    "Hindi",
    "Portuguese",
    "Russian",
    "Italian",
    "Korean",
    "Urdu",
    "Swahili",
]

# Target Systems
TARGET_SYSTEMS = [
    "Claude (claude.ai)",
    "Claude (Claude Code)",
    "Gemini (webapp)",
    "Gemini (CLI)",
    "Gemini (Workspace)",
    "Notion AI",
    "Le Chat",
    "Kagi Assistant",
    "Raycast AI",
    "Confer",
    "Fellou Browser",
]

# Target Behaviors (Attack Goals)
TARGET_BEHAVIORS = [
    "System prompt extraction",
    "Constraint override",
    "Tool enumeration",
    "Data exfiltration",
    "Code execution",
    "Privilege escalation",
    "Unauthorized action",
    "Context leakage",
    "Constraint erosion",
    "Constraint probing",
    "Constraint bypass",
    "Constraint weakening",
]

# Default configurations
DEFAULT_BATCH_SIZE = 10
DEFAULT_MAX_RETRIES = 3
DEFAULT_TIMEOUT = 60
DEFAULT_SEED = 42
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 2048
CONFIDENCE_LEVEL = 0.95
