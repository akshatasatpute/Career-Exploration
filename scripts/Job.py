#%pip install fpdf2



import io
import tempfile
from io import BytesIO
from fpdf import FPDF, HTMLMixin
import pandas as pd
import streamlit as st
import base64
import requests
import PIL.Image as Image
from PIL import Image 
import boto3
import base64
import requests
import PIL.Image as Image

class PDF(FPDF,HTMLMixin):
    def __init__(self, width, height):
        super().__init__('P', 'mm', (width, height))
        self.width = width
        self.height = height
    def header(self):
         # Reset the text color to black before adding the header
        self.set_text_color(0, 0, 0)
        
        
        # Load the original image
        from PIL import Image
        from PIL import ImageShow
        # Open the PNG image file
        
# Function to get image from URL
        def get_image_from_url(image_url):
            response = requests.get(image_url)
            img = Image.open(io.BytesIO(response.content))
            return img
# URL of the image from Supabase
        image_url = "https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/VS-logo.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vVlMtbG9nby5wbmciLCJpYXQiOjE3MzM3MTUwOTQsImV4cCI6MTczNDMxOTg5NH0.gtfDA2Hhzeu12q9j4Ee8maC6jMLvFicS0O9xwdToXn8&t=2024-12-09T03%3A31%3A28.858Z"
        img = get_image_from_url(image_url)
        # Function to get image from URL
        def get_image_from_url(image_url):
            response = requests.get(image_url)
            img = Image.open(io.BytesIO(response.content))
            return img
# URL of the image from Supabase
        image_url = "https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/Watermark.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vV2F0ZXJtYXJrLnBuZyIsImlhdCI6MTczMzcxNTEyMiwiZXhwIjoxNzM0MzE5OTIyfQ.nO6QFtU94xh6B8K5J-MAYUvS4hHJwjfm46BpHEhod1o&t=2024-12-09T03%3A31%3A57.073Z"
# Load the image from the URL
        bg_image = get_image_from_url(image_url)
        #bg_image = r"C:\Users\User\Desktop\Career-Exploration-main\graphics\Watermark.png"
        #Set the background image as the page background
        temp_bg_file = tempfile.mktemp(suffix=".png")
        bg_image.save(temp_bg_file, format="PNG")
        self.image(temp_bg_file, x=50, y=50, w=self.width/2, h=self.height/2)
        # Load the logo
        #logo = r"C:\Users\User\Desktop\Career-Exploration-main\graphics\VS-logo.png"
        #img = Image.open(logo)
        
        # Save the logo to a temporary file
        temp_image_file = tempfile.mktemp(suffix=".png")
        img.save(temp_image_file, format="PNG")
       
        
        # Define logo size
        logo_width = 26  # You can adjust the size as you need
        logo_height = 20  # You can adjust the size as you need
        # Add the logo on the top right corner
        self.image(temp_image_file, x = self.width - logo_width - 10, y = 10, w = logo_width, h = logo_height)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Career Exploration Report', 0, 1, 'C')
        self.cell(0, 10, '', 0, 1, 'C')
        
    
    def add_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'C')
        self.cell(0, 10, '', 0, 1, 'C')
       
    def add_college_details_title(self):
        self.add_title('College Details Report')
    def add_job_details_title(self):
        self.add_title('Job Details Report')
    def add_scholarship_details_title(self):
        self.add_title('Scholarship Details Report')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
    def chapter_body(self, content):
        self.set_font('Arial', '', 12)
        line_height = 5  # Set the desired interline spacing
        lines = content.split('\n')
        for line in lines:
            if ":" in line:
                # If the line contains a colon (":"), consider it as a content header and display it in bold
                parts = line.split(":")
                self.set_font('Arial', 'B', 12)
                self.cell(0, line_height, txt=parts[0] + ":", ln=False)
                self.set_font('Arial', '', 12)
                self.cell(0, line_height, txt=parts[1], ln=True)
            else:
                self.cell(0, line_height, txt=line, ln=True)
        self.ln()
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        
        # Set the text color to black before adding page numbers
        self.set_text_color(0, 0, 0)
        
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')
        # Reset text color to black
        self.set_text_color(0, 0, 0)
        
    def add_bold_text(self, text):
        self.set_font('Arial', 'B', 12)
        line_height = 5  # Set the desired interline spacing
        lines = text.split('\n')
        for line in lines:
            self.cell(0, line_height, txt=line, ln=True)
        self.ln()  # Add a line after each detail
        self.set_font('Arial', '', 12)  # Set the font back to normal for the next line
        
    def add_scholarship_table(self, data):
        # Set column names for the table
        column_names = ['Scholarship Name']
        # Set column widths
        col_widths = [100]
        # Set font for table header
        self.set_font('Arial', 'B', 12)
        # Add table header
        for name, width in zip(column_names, col_widths):
            self.cell(width, 10, str(name), 1, 0, 'C')
        self.ln()
        # Set font for table content
        self.set_font('Arial', '', 10)  # Reduce font size to fit the content
        # Add table content
        for row in data:
            for item, width in zip(row, col_widths):
                self.cell(width, 8, str(item).encode('latin-1', 'replace').decode('latin-1'), 1, 0, 'C')
            self.ln()
    def add_scholarship_offered_by_table(self, data):
        column_names = ['Offered by', 'Govt./Private', 'For study in']
        col_widths = [70, 40, 60]
        self.set_font('Arial', 'B', 12)
        # Ensure the column names have the same number of elements as col_widths
        assert len(column_names) == len(col_widths)
        for name, width in zip(column_names, col_widths):
            self.cell(width, 10, str(name), 1, 0, 'C')
        self.ln()
        self.set_font('Arial', '', 10)
        for row in data:
            assert len(row) == len(col_widths)
            for item, width in zip(row, col_widths):
                self.cell(width, 8, str(item).encode('latin-1', 'replace').decode('latin-1'), 1, 0, 'C')
            self.ln()
    def add_scholarship_duration_table(self, data):
        column_names = ['Duration', 'Award amount', 'Application deadline']
        col_widths = [70, 40, 60]
        self.set_font('Arial', 'B', 12)
        assert len(column_names) == len(col_widths)
        for name, width in zip(column_names, col_widths):
            self.cell(width, 10, str(name), 1, 0, 'C')
        self.ln()
        self.set_font('Arial', '', 10)
        for row in data:
            for item, width in zip(row, col_widths):
                self.cell(width, 8, str(item).encode('latin-1', 'replace').decode('latin-1'), 1, 0, 'C')
            self.ln()
            
    def add_scholarship_details(self, scholarship_name, details):
        # Set font for scholarship details content
        self.set_font('Arial', '', 12)
        # Define the width for the keys and values
        key_width = 60
        value_width = self.w - key_width - self.r_margin - self.l_margin
        # Define the space after the colon for value
        colon_space = 4  # Adjust this value as needed
        
        # Loop through scholarship details and add them to the PDF
        for key, value in details.items():
            # Convert the key and value to strings using 'utf-8' encoding
            key_str = str(key).encode('latin-1', 'replace').decode('latin-1')
            value_str = str(value).encode('latin-1', 'replace').decode('latin-1')
                
        # Calculate the combined width of key and value
            # Calculate the width of the key without considering value or colon
            key_colon_width = self.get_string_width(key_str + ": ")
        
        # Check if the combined width fits within the available width
            if key_colon_width + self.get_string_width(value_str) <= value_width:
            # Set font to bold for the key
                self.set_font('Arial', 'B', 12)
                # Print the key in bold
                self.cell(key_colon_width, 8, txt=f"{key_str}:", ln=False)
            # Reset font to regular for the value
                self.set_font('Arial', '', 12)
                
                # Check if the value is a URL
                if "http" in value:
                # Set the text color to blue
                    self.set_text_color(0, 0, 255)
                    
                # Print the wrapped value
                self.cell(colon_space)  # Add the desired space after the colon
                self.cell(0, 8, txt=value_str, ln=True)
                # Reset text color to black
                self.set_text_color(0, 0, 0)
            else:
                # Set font to bold for the key
                self.set_font('Arial', 'B', 12)
                # Print the key in bold with a colon
                self.cell(0, 8, txt=f"{key_str}:", ln=True)
                # Reset font back to normal for the value
                self.set_font('Arial', '', 12)
                # Print wrapped value
                # Check if the value is a URL
                if "http" in value:
                # Set the text color to blue
                    self.set_text_color(0, 0, 255)
            # Print the wrapped value
                self.multi_cell(self.w - self.r_margin - self.l_margin, 8, txt=value_str, align='L')
            # Reset text color to black
                self.set_text_color(0, 0, 0)
        self.ln()
        # Reset font back to normal
        self.set_font('Arial', '', 12)
        
def add_detail(self, detail, separator="\n"):
    # Split into column name and value
    column_name, value = detail.split(": ", 1)
    # Remove leading and trailing whitespace from the value
    value = value.strip()
    # Replace newline characters with spaces in the value
    value = value.replace("\n", " ")
    # Check for URL and set color
    url_detected = "http" in value or "www." in value
    # Set font for column name (bold) and value (regular)
    self.set_font('Arial', 'B', 12)
    # Calculate width for the value
    value_width = self.w - self.l_margin - self.r_margin
    # Check if the value is longer than the available space
    if self.get_string_width(column_name) + self.get_string_width(": ") + self.get_string_width(value) <= value_width:
        # Print column name
        self.cell(self.get_string_width(column_name) + self.get_string_width(": "), 7, txt=column_name + ": ", ln=False)
        # Print value
        self.set_font('Arial', '', 12)
        
        # Set text color to blue if URL is detected
        if url_detected:
            self.set_text_color(0, 0, 255)  # Set text color to blue
        
        self.multi_cell(value_width - self.get_string_width(column_name) - self.get_string_width(": "), 7, txt=value, align='L')
        
        # Reset text color to black
        self.set_text_color(0, 0, 0)
    else:
        # Print concatenated column name and value with a 2-space gap
        column_value = f"{column_name}:  "
        self.cell(0, 7, txt=column_value, ln=True)
        # Reset font to regular for value
        self.set_font('Arial', '', 12)
        # Split multi-line value into individual lines
        lines = value.split('\n')
        for line in lines:
            # Check for URL and set color
            url_detected = "http" in line or "www." in line
            
            if url_detected:
                self.set_text_color(0, 0, 255)  # Set text color to blue
        # Print value
            self.multi_cell(value_width, 7, txt=value, align='L')  # Adjust line_height as needed
        # Reset text color to black
        self.set_text_color(0, 0, 0)
    # Add the custom separator after each detail
    self.set_font('Arial', '', 5)  # Adjust font size for the separator
    self.cell(0, 2, separator, ln=True)
# Load the Excel file into a pandas DataFrame
# Load the Excel file into a pandas DataFrame
#s3=pd.read_excel(r"C:\Users\User\Desktop\Career-Exploration-main\data_files\Job_S3.xlsx")
import requests
import pandas as pd
from io import BytesIO
# URL pointing to the CSV file
file_url = 'https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/Job_S3.xlsx?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vSm9iX1MzLnhsc3giLCJpYXQiOjE3MzM1MTI3MjAsImV4cCI6MTczNDExNzUyMH0.zQfwABwUJtnA41UQ_Q8L8YbYZkBfGfxsiM5iXHbQ5fo&t=2024-12-06T19%3A18%3A41.253Z'
try:
    response = requests.get(file_url)
    response.raise_for_status()  # Raise an error for bad status codes
    # Read the content of the response as a pandas DataFrame, specifying the appropriate encoding
    dp = pd.read_csv(BytesIO(response.content), encoding='latin1')  # You can try 'latin1' encoding as an alternative
    # Proceed with processing the data in the dataframe 'df'
except requests.exceptions.RequestException as e:
    print("An error occurred while accessing the CSV file:", e)
except Exception as e:
    print("An error occurred while reading the CSV file:", e)
#dp = pd.read_excel(r"C:\Users\User\Desktop\Career-Exploration-main\data_files\Job_S3.xlsx")
#dp = load_job_details()
dp.head()
@st.cache_resource
def load_job_details(selected_field):
    filtered_job_titles = dp[dp['Field'] == selected_field]['Job Titles'].unique()
    return filtered_job_titles
def clean_text(text):
    try:
        return text.encode('latin-1', 'replace').decode('latin-1')
    except UnicodeEncodeError:
        return "[Non-Latin-1 Character]"
    
def main():
    st.title('Job Details Report')
    selected_field = st.session_state.selected_field
    filtered_job_titles = load_job_details(selected_field)
    if len(filtered_job_titles) == 0:
        st.error(f"No job titles found for the selected field: **{selected_field}**")
        st.error("*Please choose a different field and job title below:*")
        fields = sorted(list(dp['Field'].unique()))  # Sort the fields
        fields.insert(0, 'Select a field')  # Add a default option
        selected_field = st.selectbox('**Select Field**', fields)
        if selected_field == 'Select a field':
            st.warning("Please select a field.")
            return
        #st.session_state.selected_field = selected_field
        filtered_job_titles = load_job_details(selected_field)
        
        # Use len() to check if the array is empty
        if len(filtered_job_titles) == 0:
            filtered_job_titles = ['Select a job title']  # Add a default option
        else:
            filtered_job_titles = sorted(filtered_job_titles)  # Sort the job titles
        selected_job_title = st.selectbox('**Select Job Title**', filtered_job_titles)
    else:
        selected_job_title = st.selectbox('**Select Job Title**', sorted(filtered_job_titles))  # Sort the job titles
    if selected_job_title:
        job_details = dp[(dp['Field'] == selected_field) & (dp['Job Titles'] == selected_job_title)]
        st.header('Job Details')
        st.markdown(f"**Field:** {selected_field}")
        st.markdown(f"**Job Title:** {selected_job_title}")
        st.markdown(f"**Job Description:** {job_details['Job Description'].values[0]}")
        st.markdown(f"**Work Environment:** {job_details['Work Environment'].values[0]}")
       # st.markdown(f"**Women Role Models**: {st.session_state.college_details['Women role models'].values[0]}")
        st.markdown(f"**Key Competency:** {job_details['Key Competancy'].values[0]}")
        st.markdown(f"**Available Skill Training Schemes:** {job_details['Available skill training schemes'].values[0]}")
        st.markdown(f"**Sample Training & Courses:** {job_details['Sample training & courses'].values[0]}")
        st.markdown(f"**Career Path Progression:** {job_details['Career path progression'].values[0]}")
        st.markdown(f"**Probable Employers:** {job_details['Probable Employers'].values[0]}")
        #st.markdown(f"**Salary:** {job_details['Salary'].values[0]}")
        
        # Load the data from Excel into a DataFrame
        #df= load_sco_details()
        # URL pointing to the CSV file
        file_url = 'https://jyrdwnpjlcznlvqxmthc.supabase.co/storage/v1/object/sign/Career%20Exploration/Scholarship_S3.xlsx?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJDYXJlZXIgRXhwbG9yYXRpb24vU2Nob2xhcnNoaXBfUzMueGxzeCIsImlhdCI6MTczMzUxMjc0MywiZXhwIjoxNzM0MTE3NTQzfQ.JzGv8Mub-PS_GJKOVUyZMj7NS_oGRofX6wlJodoX9EI&t=2024-12-06T19%3A19%3A03.629Z'
        try:
            response = requests.get(file_url)
            response.raise_for_status()  # Raise an error for bad status codes
        # Read the content of the response as a pandas DataFrame, specifying the appropriate encoding
            df = pd.read_csv(BytesIO(response.content), encoding='latin1')  # You can try 'latin1' encoding as an alternative
    # Proceed with processing the data in the dataframe 'df'
        except requests.exceptions.RequestException as e:
            print("An error occurred while accessing the CSV file:", e)
        except Exception as e:
            print("An error occurred while reading the CSV file:", e)
        #df = pd.read_excel(r"C:\Users\User\Desktop\Career-Exploration-main\data_files\Scholarship_S3.xlsx")
        # Filter the DataFrame to only include rows where Field is 'Science'
        df_science = df[df['Field'] == 'Science']
        # Filter the DataFrame for the selected field
        df_selected = df[df['Field'] == selected_field]
        # Concatenate the df_science and df_selected DataFrames
        df_concat = pd.concat([df_science, df_selected])
        # Create a PDF object
        pdf = PDF(210, 297)
        # Add a page
        pdf.add_page()
        pdf.set_left_margin(20)  # Adjust the left margin (default is 10 mm)
        pdf.set_right_margin(20)  
        # Set font 
        pdf.set_font("Arial", "B", 14)
        # Add title
        pdf.add_college_details_title()
        # Add content
        college_content = [
            f"Student Name: {st.session_state.student_name}",
            f"Qualified Degree: {st.session_state.selected_degree}",
            f"Field: {st.session_state.selected_field}",
            f"Subfield: {st.session_state.selected_subfield}",
            f"College: {st.session_state.selected_college}",
            f"Duration: {st.session_state.college_details['Duration'].values[0]}",
            f"College Fee: {st.session_state.college_details['Fees'].values[0]}"
            #f"Application process: {st.session_state.college_details['Application process'].values[0]}",
            #f"Application deadline: {st.session_state.college_details['Application deadline'].values[0]}",
            #f"NIRF and Other Rank (2022): {st.session_state.college_details['NIRF AND OTHER RANK(2022)'].values[0]}",
            #f"Minimum Marks for Eligibility: {st.session_state.college_details['MIN MARKS FOR ELIGIBILITY'].values[0]}",
            #f"Entrance Name and Duration: {st.session_state.college_details['ENTRANCE NAME AND DURATION'].values[0]}",
            #f"Exam Details: {st.session_state.college_details['EXAM DETAILS'].values[0]}",
            #f"Test Date: {st.session_state.college_details['TEST DATE'].values[0]}",
            #f"Application Process: {st.session_state.college_details['Application process'].values[0]}",
            #f"Application Fee: {st.session_state.college_details['APPLICATION FEE'].values[0]}",
            #f"Selection Process: {st.session_state.college_details['Selection Process'].values[0]}",
            #f"Intake: {st.session_state.college_details['INTAKE'].values[0]}",
            #f"Link: {st.session_state.college_details['LINK'].values[0]}",
            #f"Award amount: {st.session_state.college_details['Award amount'].values[0]}",
            #f"Things covered by the award: {st.session_state.college_details['Things covered by the award'].values[0]}",
            #f"Contact website: {st.session_state.college_details['Contact website'].values[0]}",
            #f"Scholarships for this College: {st.session_state.college_details['Scholarship Name'].values[0]}"
        ]
       # Add college content to the PDF
        for line in college_content:
            # Replace non-latin-1 characters
            line_cleaned = line.encode('latin-1', 'replace').decode('latin-1')
            add_detail(pdf, line_cleaned)
        # Draw a separator line after college content
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(10) # Add space after the separator line
         # Set font 
        pdf.set_font("Arial", "B", 14)
        # Add title
        pdf.add_job_details_title()
        # Add content
        job_content = [
            f"Job Title: {selected_job_title}",
            f"Job Description: {job_details['Job Description'].values[0]}",
            f"Work Environment: {job_details['Work Environment'].values[0]}",
           # f"Women Role Models: {st.session_state.college_details['Women role models'].values[0]}"
            f"Key Competancy: {job_details['Key Competancy'].values[0]}",
            f"Available Skill Training Schemes: {job_details['Available skill training schemes'].values[0]}",
            f"Sample Training & Courses: {job_details['Sample training & courses'].values[0]}",
            f"Career Path Progression: {job_details['Career path progression'].values[0]}",
            f"Probable Employers: {job_details['Probable Employers'].values[0]}",
           # f"Salary: {job_details['Salary'].values[0]}"
        ]
        # Add job content to the PDF
        for line in job_content:
            # Replace non-latin-1 characters
            line_cleaned = line.encode('latin-1', 'replace').decode('latin-1')
            add_detail(pdf, line_cleaned)
            
        # Draw a separator line after job content
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(10)
            
        # Set font for the "Scholarship Details" section to bold
        pdf.set_font("Arial", "B", 14)
        # Initialize a flag to check if the scholarship details title has been printed
        printed_title = False
        
        # Group scholarship details by 'Scholarship Name' and loop through each group
        grouped_scholarships = df_concat.groupby('Scholarship Name')
        bullet_counter = 1  # Initialize the bullet counter
        
        for scholarship_name, scholarship_group in grouped_scholarships:
            # Check if the selected degree matches the degree in the scholarship details
            if st.session_state.selected_degree == 'Masters':
                # Only add the scholarship details title once
                if not printed_title:
                    pdf.add_scholarship_details_title()
                    printed_title = True
                    
                # Add scholarship name with bullet point to the PDF
                bullet_text = f"{bullet_counter}. Scholarship Name: {scholarship_name}"
                pdf.add_bold_text(bullet_text)
            
                # Add scholarship tables to the PDF
                pdf.add_scholarship_offered_by_table(scholarship_group[['Offered by', 'Govt./Private', 'For study in']].values)
                pdf.add_scholarship_duration_table(scholarship_group[['Duration', 'Award amount', 'Application deadline']].values)
            
                # Add a gap after the scholarship table
                pdf.ln(5)  # Adjust the gap size as needed
                # Create a dictionary with scholarship details for printing
                scholarship_details = scholarship_group.iloc[0].to_dict()
                scholarship_details.pop('Degree', None)
                scholarship_details.pop('Field', None)
                scholarship_details.pop('Subfield', None)
                scholarship_details.pop('Scholarship Name', None)
                scholarship_details.pop('Offered by', None)
                scholarship_details.pop('Govt./Private', None)
                scholarship_details.pop('For study in', None)
                scholarship_details.pop('Duration', None)
                scholarship_details.pop('Award amount', None)
                scholarship_details.pop('Application deadline', None)
                # Add scholarship details to the PDF
                pdf.add_scholarship_details(scholarship_name, scholarship_details)
                # Additional space after scholarship details
                pdf.ln(5)
                # Increment the bullet counter for the next scholarship
                bullet_counter += 1
                
            
    try:
        # Generate the PDF document
        pdf_output = pdf.output(dest="S")
        
        # Check if the PDF output is not empty
        if pdf_output:
            # Convert the bytearray to bytes
            pdf_bytes = bytes(pdf_output)
            # Encode the bytes as base64
            pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
            # Display the download button
            st.markdown(
                f'<a href="data:application/pdf;base64,{pdf_base64}" download="{st.session_state.student_name}_progress_report.pdf">Download PDF</a>',
                unsafe_allow_html=True
            )
        else:
            st.error("PDF output is empty. Please check the PDF generation process.")
    except Exception as e:
        st.error(f"Error occurred during PDF generation: {e}")
    if st.button('Back'):
        st.session_state.next_page = False
        st.experimental_rerun()
if __name__ == '__main__':
    main()



