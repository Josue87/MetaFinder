from docx import Document
from PyPDF2 import PdfFileReader
from openpyxl import load_workbook
from pptx import Presentation


def extract_doc(document):
    metadata = {}
    doc = Document(document)
    prop = doc.core_properties
    metadata["/Author"] = prop.author
    metadata["/Comments"] = prop.comments
    metadata["/Created"] = prop.created
    metadata["/Identifier"] = prop.identifier
    metadata["/Keywords"] = prop.keywords
    metadata["/Modified"] = prop.modified
    metadata["/Subject"] = prop.subject
    metadata["/Title"] = prop.title
    return metadata

def extract_pdf(document):
    metadata = {}
    with open(document, 'rb') as f:
        pdf = PdfFileReader(f, strict=False)
        info = pdf.getDocumentInfo()
        for meta in info:
            data = info.get(meta, None)
            metadata[meta] = data
    return metadata


def extract_xls(document):
    metadata = {}
    wb = load_workbook(document)
    prop = wb.properties
    metadata["/Author"] = prop.creator
    metadata["/Comments"] = prop.description
    metadata["/Created"] = prop.created
    metadata["/Identifier"] = prop.identifier
    metadata["/Keywords"] = prop.keywords
    metadata["/Modified"] = prop.modified
    metadata["/Subject"] = prop.subject
    metadata["/Title"] = prop.title
    return metadata

def extract_ppt(document):
    pptx_presentation = Presentation(document)
    prop = pptx_presentation.core_properties
    metadata["/Author"] = prop.author
    metadata["/Comments"] = prop.comments
    metadata["/Created"] = prop.created
    metadata["/Identifier"] = prop.identifier
    metadata["/Keywords"] = prop.keywords
    metadata["/Modified"] = prop.modified
    metadata["/Subject"] = prop.subject
    metadata["/Title"] = prop.title
    return metadata


def remove_indirect_object(metadata):
    new_metadata = {}
    for m in metadata:
        value =  metadata[m]
        if "IndirectObject(" not in str(value) and str(value) != "":
            new_metadata[m] = value

    return new_metadata


def extract_metadata(document):
    try:
        if document.endswith("pdf"):
            metadata = extract_pdf(document)
        elif document.endswith("doc") or document.endswith("docx"):
            metadata = extract_doc(document)
        elif document.endswith("xls") or document.endswith("xlsx"):
            metadata = extract_xls(document)
        elif document.endswith("ppt") or document.endswith("pptx"):
            metadata = extract_ppt(document)
        else: 
            metadata = {}
    except:
        metadata = {}
  
    return remove_indirect_object(metadata)




