import os

def edit_summary(longform_name):
    f = open(str(os.path.abspath(os.getcwd())) +  "/longform_index_dir.txt", 'r')
    target_dir = f.read()
    f.close()

    file_dir = target_dir + longform_name + "/" + longform_name + " 요약본.md"

    f = open(file_dir, 'r')
    summary_lines = f.readlines()
    f.close()

    found_title = False
    
    editted_summary = ""

    for summary_line in summary_lines:
        if not found_title:
            if summary_line[0:2] == "# ":
                found_title = True
            editted_summary += summary_line
        
        else:
            if summary_line[0:4] == "----":
                found_title = False
                editted_summary += summary_line
            
            if summary_line[0:2] == "# ":
                editted_summary += summary_line
        
    f = open(file_dir, 'w')
    f.write(editted_summary)
    f.close()

if __name__ == "__main__":
   edit_summary("거시경제이론")
   edit_summary("선물옵션")