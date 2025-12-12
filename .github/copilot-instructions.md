# Copilot Instructions for Daily Repository

## Project Overview

This is a personal **multi-language learning and study repository** combining English study notes, music/computer science knowledge, and coding exercises. The project is not a traditional software application but rather a learning workspace and note-taking system.

**Key Purpose:** Track daily learning progress, maintain vocabulary databases, store study notes, and preserve completed coding projects.

## Project Structure & Components

### 1. **Learning & Notes (Primary Focus)**
- **`Kon/`** - English study materials
  - `English Study note.md` - Main English study documentation
  - `No.1 9-12.md` - Specific topic notes
  - `create a link.md` - Reference management
- **`dailycard/`** - Daily flashcard/study materials
  - `goodstart.md` - Daily motivation/starter notes
- **Daily markdown files** (`2025-01-02.md`, `5-26.md`, `6-1.md`, etc.) - Time-indexed daily logs

### 2. **Reference Data**
- **`词频.txt`** - Chinese word frequency database
- **`单词库文档.txt`** - Vocabulary library documentation
- **`语料库文档.txt`** - Corpus documentation
- **`10-12.txt`, `10-17.word`** - Additional vocabulary/reference files

### 3. **Coding Projects**
- **`DoneV.1/`** - Completed Visual Studio C++ project
  - `try2again/try2again.vcxproj` - Windows C++ project (archived/completed work)
- **`USD/moneyGame.py`** - Python utility (currently empty placeholder)

### 4. **Documentation**
- **`README.md`** - Project description (English language learning focus with Computer Science knowledge)

## Development Conventions & Patterns

### File Organization Patterns
1. **Date-based naming** - Most daily notes use date format (YYYY-MM-DD.md or M-D.md)
2. **Topic-based grouping** - Study materials organized by subject (Kon for English, dailycard for daily practices)
3. **Multi-language content** - Documents may contain English, Chinese, and other language materials

### Content Types
- **Study notes** - Markdown format, usually containing:
  - English vocabulary and phrases
  - Grammar explanations
  - Topic-specific learning materials
- **Reference databases** - Plain text files containing word lists, frequency data, corpus references
- **Code exercises** - Individual Python files (see `USD/moneyGame.py` as placeholder)

## Working with This Repository

### When Adding New Study Materials
- Use date-based naming for daily entries: `YYYY-MM-DD.md`
- Place English-specific content in `Kon/` directory
- Use markdown format for all notes
- Organize vocabulary updates into `词频.txt` or `单词库文档.txt`

### When Modifying Vocabulary Data
- `词频.txt` - Update word frequency lists here
- `单词库文档.txt` - Maintain structured vocabulary database with definitions/examples
- `语料库文档.txt` - Track corpus references and language examples

### When Working with Code Projects
- C++ projects in `DoneV.1/` are completed/archived - use as reference only
- New Python exercises go in `USD/` directory
- Keep code utilities focused on learning goals (e.g., `moneyGame.py` for financial calculation practice)

## Language & Content Notes

- **Primary languages in repository:** English (study focus), Chinese (reference materials)
- **May add support for:** Korean, Japanese (mentioned in README as future possibilities)
- **Content style:** Educational, personal learning journal format

## Important Conventions

1. **This is NOT a production codebase** - Focus on learning and knowledge organization
2. **Preserved vs. Active:**
   - `DoneV.1/` projects are preserved learning artifacts
   - Current work goes in time-indexed markdown files
3. **Multilingual support** - Be prepared for mixed-language content in single files
4. **Obsidian integration** - `.obsidian/` folder present in `Kon/` indicates Obsidian vault usage for note-taking

## Key Files to Reference

- `README.md` - Overall project motivation and scope
- `Kon/English Study note.md` - Primary English study documentation
- `词频.txt` - Vocabulary reference standard format
