import re
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_classic.schema import Document

SECTION_HEADERS = [
    "SUMMARY",
    "SKILLS",
    "TECHNICAL SKILLS",
    "EXPERIENCE",
    "WORK EXPERIENCE",
    "EDUCATION",
    "PROJECTS",
    "INTERNSHIPS",
    "CERTIFICATIONS"
]


def clean_text(text: str) -> str:
    """
    Fix character spaced text and noisy formatting from PDFs
    """
    text = re.sub(r'(?<=\w)\s(?=\w)', '', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()


def split_by_sections(doc: Document):
    """
    Split resume into semantic sections
    """
    chunks = []
    text = doc.page_content

    # Regex pattern for headers
    pattern = "|".join([fr"\n{h}\n" for h in SECTION_HEADERS])
    sections = re.split(pattern, text, flags=re.IGNORECASE)

    for section in sections:
        section = section.strip()
        if len(section) > 200:
            chunks.append(
                Document(
                    page_content=section,
                    metadata=doc.metadata
                )
            )

    return chunks


def load_resumes(folder_path: str):
    final_chunks = []

    for file in Path(folder_path).iterdir():
        if file.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file))
        elif file.suffix.lower() == ".docx":
            loader = Docx2txtLoader(str(file))
        else:
            continue

        for doc in loader.load():
            # ✅ Clean text
            doc.page_content = clean_text(doc.page_content)

            # ✅ Attach metadata
            doc.metadata["candidate_id"] = file.stem
            doc.metadata["source"] = str(file)

            # ✅ Section-aware chunking
            chunks = split_by_sections(doc)
            final_chunks.extend(chunks)

    return final_chunks
