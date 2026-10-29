import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      clian_text = ""
      html_tag = False
      for i in html:
          if i == '<':
              html_tag = True
          elif i == '>':
              html_tag = False
          elif not html_tag:
              clian_text += i
      with codecs.open(result_file, 'w', 'utf-8') as file:
          file.write(clian_text)