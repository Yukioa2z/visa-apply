#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const skillName = "visa-apply";
const packageRoot = path.resolve(__dirname, "..");
const sourceDir = path.join(packageRoot, "skill");

function usage() {
  console.log(`Install ${skillName}

Choose where to install with --dest — your agent's skills directory:
  Claude Code   npx @yukioa2z/visa-apply -- --dest ~/.claude/skills
  Codex         npx @yukioa2z/visa-apply -- --dest ~/.codex/skills
  Other agent   npx @yukioa2z/visa-apply -- --dest <your agent's skills dir>

Options:
  --dest <path>   Skill root directory (required).
  --dry-run       Print the destination without copying files.
  --help          Show this help message.
`);
}

function expandHome(value) {
  if (!value) return value;
  if (value === "~") return os.homedir();
  if (value.startsWith("~/")) return path.join(os.homedir(), value.slice(2));
  return value;
}

function readOption(name) {
  const args = process.argv.slice(2);
  const index = args.indexOf(name);
  if (index === -1) return undefined;
  return args[index + 1];
}

const args = process.argv.slice(2);
if (args.includes("--help") || args.includes("-h")) {
  usage();
  process.exit(0);
}

if (!fs.existsSync(sourceDir)) {
  console.error(`Skill source not found: ${sourceDir}`);
  process.exit(1);
}

const destOption = readOption("--dest");
if (!destOption) {
  console.error(
    "No --dest given. Install into your agent's skills directory:\n"
  );
  usage();
  process.exit(1);
}

const destRoot = path.resolve(expandHome(destOption));
const destDir = path.join(destRoot, skillName);

if (args.includes("--dry-run")) {
  console.log(destDir);
  process.exit(0);
}

fs.mkdirSync(destRoot, { recursive: true });
fs.rmSync(destDir, { recursive: true, force: true });
fs.cpSync(sourceDir, destDir, { recursive: true });

console.log(`Installed ${skillName} to ${destDir}`);
console.log(`Try: Use $${skillName} to check your visa need and prepare an application dossier.`);
