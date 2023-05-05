# import os
# import json
# from lxml import etree

# def list_html_files(startpath):
#     """
#     This function returns a list of all HTML files in the given directory
#     and its subdirectories recursively.
#     """
#     html_files = []
#     for root, dirs, files in os.walk(startpath):
#         for file in files:
#             if file.endswith('.html'):
#                 html_files.append(os.path.join(root, file))
#     return html_files

# def extract_text(element):
#     """
#     This function extracts the text content from an lxml element and returns it as a string.
#     """
#     if element is not None:
#         return ' '.join(element.xpath('.//text()')).strip()
#     return ''

# def create_indexable_json_object(html_file):
#     """
#     This function creates an indexable JSON object for an HTML file.
#     It extracts the page title and body content, and returns the object as a dictionary.
#     """
#     with open(html_file) as f:
#         content = f.read()
#         parser = etree.HTMLParser()
#         tree = etree.fromstring(content, parser)
#         title_element = tree.find('.//title')
#         body_element = tree.find('.//body')
#         title = extract_text(title_element)
#         body = extract_text(body_element)
#         data = {
#             'title': title,
#             'body': body
#         }
#         return data

# if __name__ == '__main__':
#     startpath = '.'  # Current directory
#     html_files = list_html_files(startpath)
#     json_objects = []
#     for html_file in html_files:
#         json_object = create_indexable_json_object(html_file)
#         json_objects.append(json_object)
    
#     json_output = json.dumps(json_objects, indent=2)
#     print(json_output)

import os
import json
from lxml import etree

def list_html_files(startpath):
    """
    This function returns a list of all HTML files in the given directory
    and its subdirectories recursively.
    """
    html_files = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

def extract_text(element):
    """
    This function extracts the text content from an lxml element and returns it as a string.
    """
    if element is not None:
        return ' '.join(element.xpath('.//text()')).strip()
    return ''

def create_indexable_json_object(html_file):
    """
    This function creates an indexable JSON object for an HTML file.
    It extracts the page title, body content, and URL, and returns the object as a dictionary.
    """
    with open(html_file) as f:
        content = f.read()
        parser = etree.HTMLParser()
        tree = etree.fromstring(content, parser)
        title_element = tree.find('.//title')
        body_element = tree.find('.//body')
        title = extract_text(title_element)
        body = extract_text(body_element)
        relative_path = os.path.relpath(html_file, start=startpath)
        url = f"https://tyohare.github.io/assets/{relative_path}"
        data = {
            'title': title,
            'body': body,
            'url': url
        }
        return data

if __name__ == '__main__':
    startpath = '.'  # Current directory
    html_files = list_html_files(startpath)
    json_objects = []
    for html_file in html_files:
        json_object = create_indexable_json_object(html_file)
        json_objects.append(json_object)
    
    json_output = json.dumps(json_objects, indent=2)
    print(json_output)
