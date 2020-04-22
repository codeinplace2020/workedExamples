#!/usr/bin/env python

from plugins.bottle.bottle import SimpleTemplate

import os.path
import sys
import shutil

IGNORE_DIRS = []

TEMPLATE_TEXT = open('template.html').read()

# supported image types: jpg, png


class Compiler(object):

    # Function: Run
    # -------------
    # This function compiles all the html files (recursively)
    # from the templates dir into the current folder. Folder
    # hierarchy is preserved
    def run(self):
        example_paths = []
        for dir_name in os.listdir('examples'):
            
            name = self.complile_example(dir_name)
            print(dir_name)
            example_paths.append((dir_name, name))
        self.make_home_page(example_paths)

    #####################
    # Private Helpers
    #####################

    def make_home_page(self, paths):
        example_list = ''
        for example in paths:
            (exampleId, name) = example
            example_list += '<li><a href="{}">{}</a></li>\n'.format(exampleId+'/index.html', name)
        template_text = open('home_template.html').read()
        compiled_html = SimpleTemplate(template_text).render(exampleList = example_list)
        compiled_html = compiled_html.encode('utf8')
        open(os.path.join('en', 'index.html'), 'wb').write(compiled_html)

    def complile_example(self, dir_name):
        data = {
            'html':self.load_part(dir_name, 'index.html'),
            'title':self.load_part(dir_name, 'title.txt'),
            'credit':self.load_part(dir_name, 'credit.txt'),
            'soln':self.load_part(dir_name, 'soln.py'),
            'exampleId':dir_name
        }
        out_path = os.path.join('en', dir_name, 'index.html')
        self.compile_template(out_path, data)
        self.copy_all_images(dir_name)
        return data['title']

    def copy_all_images(self, dir_name):
        out_path = os.path.join('en', dir_name)
        in_path = os.path.join('examples', dir_name)
        for file_name in os.listdir(in_path):
            file_type = file_name.split('.')[-1].lower()
            if self.is_img(file_type):
                self.copy_file(in_path, out_path, file_name)

    def copy_file(self, in_path, out_path, file_name):
        source = os.path.join(in_path, file_name)
        destination = os.path.join(out_path, file_name)
        shutil.copyfile(source, destination)

    def compile_template(self, out_path, data):
        compiled_html = SimpleTemplate(TEMPLATE_TEXT).render(
            html=data['html'],
            title=data['title'],
            credit=data['credit'],
            soln=data['soln'],
            exampleId = data['exampleId']
        )
        self.make_path(out_path)
        compiled_html = compiled_html.encode('utf8')
        open(out_path, 'wb').write(compiled_html)

    def is_img(self, file_type):
        if file_type == 'png': return True
        if file_type == 'jpg': return True
        if file_type == 'svg': return True
        return False

    def load_part(self, dir_name, file_name):
        in_path = os.path.join('examples', dir_name)
        return open(os.path.join(in_path, file_name)).read()

    def make_path(self, path):
        dirPath = os.path.dirname(path)
        if dirPath == '': return
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)



if __name__ == '__main__':
    Compiler().run()
