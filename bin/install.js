#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const skillName = "visa-apply";
const packageRoot = path.resolve(__dirname, "..");
const sourceDir = path.join(packageRoot, "skill");

function usage() {
  console.log(`Install ${skillName}

Usage:
  npx github:Yukioa2z/visa-apply
  npx github:Yukioa2z/visa-apply -- --dest ~/.claude/skills

Options:
  --dest <path>   Skill root directory. Defaults to $CODEX_HOME/skills or ~/.codex/skills.
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

const defaultRoot = process.env.CODEX_HOME
  ? path.join(process.env.CODEX_HOME, "skills")
  : path.join(os.homedir(), ".codex", "skills");

const destRoot = path.resolve(expandHome(readOption("--dest") || defaultRoot));
const destDir = path.join(destRoot, skillName);

if (args.includes("--dry-run")) {
  console.log(destDir);
  process.exit(0);
}

fs.mkdirSync(destRoot, { recursive: true });
fs.rmSync(destDir, { recursive: true, force: true });
fs.cpSync(sourceDir, destDir, { recursive: true });

console.log(`Installed ${skillName} to ${destDir}`);
console.log(`Try: Use $${skillName} to prepare a visa application dossier.`);
