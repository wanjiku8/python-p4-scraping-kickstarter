from bs4 import BeautifulSoup

def create_project_dict():
    # Read the HTML file
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    # Parse the HTML with BeautifulSoup
    kickstarter = BeautifulSoup(html, 'html.parser')
    
    # Initialize the projects dictionary
    projects = {}
    
    # Iterate through each project
    for project in kickstarter.select("li.project.grid_4"):
        try:
            # Extract title
            title = project.select("h2.bbcard_name strong a")[0].text.strip()
            
            # Extract image link
            image_link = project.select("div.project-thumbnail a img")[0]['src']
            
            # Extract description
            description = project.select("p.bbcard_blurb")[0].text.strip()
            
            # Extract location
            location = project.select("ul.project-meta span.location-name")[0].text.strip()
            
            # Extract percent funded and remove % sign
            percent_funded = project.select("ul.project-stats li.first.funded strong")[0].text.strip().replace("%", "")
            
            # Add project data to the dictionary
            projects[title] = {
                'image_link': image_link,
                'description': description,
                'location': location,
                'percent_funded': percent_funded
            }
        except IndexError:
            # Skip if any element is missing
            continue
    
    return projects

# To test the function
if __name__ == "__main__":
    projects = create_project_dict()
    for title, data in list(projects.items())[:3]:  # Print first 3 projects
        print(f"\nProject: {title}")
        print(f"Image: {data['image_link']}")
        print(f"Description: {data['description']}")
        print(f"Location: {data['location']}")
        print(f"Percent Funded: {data['percent_funded']}%")