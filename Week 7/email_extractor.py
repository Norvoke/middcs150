# CS 150 class example

"""
Extract all e-mails from a webpage.
"""

import urllib.request
import sys

# prevent Python from rejecting website certificates
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get_emails(url, search_string="mailto:", end_search='"'): 
    """
    Extract all linked e-mail addresses from webpage
    
    Extract all e-mails addresses specified in a mailto link, e.g.
    <a href="mailto:joe@example.com"> ...
    
    Args:
        url: URL of page to scrape
        search_string: Unique string preceding e-mail address (Defaults to "mailto:")
        end_search: String immediate after e-mail address (Defaults to '"')
        
    Returns:
        List of e-mail addresses
    """
    emails = []    
        
    with urllib.request.urlopen(url) as webpage:
        # Iterate through each line of webpage, just like a file
        for line in webpage:
            line = line.decode('utf-8', 'ignore')  # Obtain a string from the raw bytes
            
            # Search for instances of search_string in the line            
            begin_index = line.find(search_string)
            if begin_index != -1:
                begin_index += len(search_string)  # Advance to first letter in address
                end_index = line.find(end_search, begin_index)  # Find ending quote
                emails.append(line[begin_index:end_index])  # Extract email address               
        return emails
            

def write_list_to_file(emails, output_file):
    """
    Write out all emails to a file

    Args:
        emails: iterable of e-mail addresses
        output_file: path of output file
    """
    with open(output_file, "w") as file:
        file.write("Email addresses:\n")
        for email in emails:
            file.write(email + "\n")    

def print_usage():
    print("python3 email_extractor.py <URL> <OUT_FILE>")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()
    else:
        url = sys.argv[1]
        outfile = sys.argv[2]
        emails = get_emails(url)
        write_list_to_file(emails, outfile)
