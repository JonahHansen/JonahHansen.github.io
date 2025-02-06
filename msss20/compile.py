def fill_template(template_text, title, contents_text):
    new_text = template_text.replace('!!title!!', title
        ).replace('!!template!!', contents_text)
    return new_text

def make_template(name: str, title: str):
    with open('new_content/_template.html') as f_template:
        template_text = f_template.read()
        with open(f'new_content/_{name}.html') as f_contents:
            with open(f'{name}.html', 'w') as f_to:
                f_to.write(fill_template(
                    template_text,
                    title,
                    f_contents.read()))

names = ['index',
         'antiharassment',
         'canberra',
         'programme',
         'participants',
         'registration',
        ]
titles = ['Home',
          'Anti-harassment Policy',
          'Visiting Canberra',
          'Programme',
          'Participants',
          'Registration',
         ]

for name, title in zip(names, titles):
    make_template(name, title)
