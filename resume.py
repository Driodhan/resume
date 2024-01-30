import streamlit as st

def main():
    st.title("Curriculum Vitae - Your Name")

    # Personal Information
    st.header("Personal Information")
    st.write("- **Name:** Your Name")
    st.write("- **Email:** your.email@example.com")
    st.write("- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/yourusername)")
    st.write("- **GitHub:** [GitHub Profile](https://github.com/yourusername)")
    st.write("- **Website:** [Personal Website](https://www.yourwebsite.com)")

    # Summary
    st.header("Summary")
    st.write("I am a passionate and dedicated individual with a background in [your field]. "
             "I possess strong [skills or qualities] and have experience in [mention specific experience].")

    # Education
    st.header("Education")
    st.subheader("Bachelor of Science in Computer Science")
    st.write("University Name, Graduation Year")

    # Work Experience
    st.header("Work Experience")
    st.subheader("Software Developer at XYZ Company")
    st.write("- Worked on [project details]")
    st.write("- Collaborated with [team members] to achieve [specific goals]")
    st.write("- Implemented [features or improvements]")

    # Skills
    st.header("Skills")
    st.write("- Programming Languages: [List languages you are proficient in]")
    st.write("- Web Technologies: [List web-related technologies]")
    st.write("- Database: [List databases]")
    st.write("- Version Control: [List version control systems]")
    st.write("- Problem Solving")
    st.write("- Team Collaboration")

    # Projects
    st.header("Projects")
    st.subheader("Project Name 1")
    st.write("- Description of the project and your role.")
    st.write("- Technologies used: [List technologies]")

    st.subheader("Project Name 2")
    st.write("- Description of the project and your role.")
    st.write("- Technologies used: [List technologies]")

    # Certifications
    st.header("Certifications")
    st.write("- Certification Name, Issuing Organization, Year")

    # Awards and Achievements
    st.header("Awards and Achievements")
    st.write("- [List any awards or achievements]")

    # Languages
    st.header("Languages")
    st.write("- English: Fluent")
    st.write("- [Any other languages]")

    # Hobbies
    st.header("Hobbies")
    st.write("- [List hobbies or interests]")

    # References
    st.header("References")
    st.write("Available upon request.")

if __name__ == '__main__':
    main()
