from todoist_api_python.api import TodoistAPI

with open("api.token", "r") as key_in:
	api = TodoistAPI(str(key_in.readlines()[0].split("\n")[0]))

def get_tasks(p_id):
	tasks=api.get_tasks()
	tasks_out = []
	for task in tasks:
		if int(task.project_id) == p_id and task.is_completed == False:
			tasks_out.append((task.content, get_attachment_from_comment(get_comments(task.id))))
	return tasks_out
			
def get_comments(t_id):
	try:
		comments=api.get_comments(task_id=t_id)
		return comments[0]
	except Exception as error:
		pass
		
def get_attachment_from_comment(comment):
	try:
		return comment.attachment.file_url
	except Exception as error:
		pass

def gen_head(title): 
    return f'''<html><head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="main.css"/>
    </head>
    <body>
    <div class="content" id="content"><p>{title}</p></div>'''


def gen_p(text, img_src):
    return f'''<div class="content" id="content"><p id="entry">{text}</p><img class="teaser-img" src={img_src}/></div>'''

def gen_tail():
    return f'''</div></body></html>'''

def main_test():
	project_id = 2294556610
	task_data = get_tasks(project_id)
	html_stream = ""
	html_stream += gen_head("peek into our fluffy fridge!")
	for t_data in task_data:
		html_stream += gen_p(t_data[0], t_data[1])
	html_stream += gen_tail()

	with open("index.html", "w") as out_html:
		out_html.write(html_stream)
 
main_test()

