prev_job_col = ["#",'Retail / customer service',
 'Food service / hospitality',
 'Office or clerical work',
 'Youth mentoring or childcare',
 'Internship / fellowship',
 'Family business / informal work']

prev_job_map = {
    "#": "#",
    "Retail / customer service": "Retail/service",
    "Food service / hospitality": "Food/hospitality",
    "Office or clerical work": "Office work",
    "Youth mentoring or childcare": "Youth/childcare",
    "Internship / fellowship": "Internship",
    "Family business / informal work": "Family/informal"
}

demograpics_map = {
    "#": "#",
    "Currently enrolled in 2/4-year college": "2/4-yr College",
    "High school graduate* (not in school)*": "HS Grad (not in school)",
    "Recently graduated from college": "Recent College Grad",
    "In high school": "In HS",
    "Enrolled in a trade or apprenticeship program": "Trade/Apprenticeship"
}


prev_job_col = ["#",'Retail / customer service',
 'Food service / hospitality',
 'Office or clerical work',
 'Youth mentoring or childcare',
 'Internship / fellowship',
 'Family business / informal work']

prev_job_map = {
    "#": "#",
    "Retail / customer service": "Retail/service",
    "Food service / hospitality": "Food/hospitality",
    "Office or clerical work": "Office work",
    "Youth mentoring or childcare": "Youth/childcare",
    "Internship / fellowship": "Internship",
    "Family business / informal work": "Family/informal"
}

goal_of_participation = ["#", 'Build professional experience',
 'Improve job readiness and soft skills',
 'Learn about career options',
 'Grow my resume or LinkedIn profile',
 'Network with professionals',
 'Gain mentorship and guidance',
 'Improve my financial knowledge']

goal_participation_map = {
    "#": "#",
    "Build professional experience": "Professional exp.",
    "Improve job readiness and soft skills": "Job readiness",
    "Learn about career options": "Explore careers",
    "Grow my resume or LinkedIn profile": "Grow resume/LinkedIn",
    "Network with professionals": "Networking",
    "Gain mentorship and guidance": "Mentorship",
    "Improve my financial knowledge": "Financial knowledge"
}

career_consideration_col = [ "#",'Personal passion',
 'High salary potential',
 'Flexibility and lifestyle fit',
 'Job market demand',
 'Role models or mentors in that field',
 'Alignment with my values and interests',
 'Previous experience or exposure',
 'Related to my natural skills and abilities']

career_consideration_map = {
    "#": "#",
    "Personal passion": "Passion",
    "High salary potential": "High salary",
    "Flexibility and lifestyle fit": "Flexibility/lifestyle",
    "Job market demand": "Market demand",
    "Role models or mentors in that field": "Role models",
    "Alignment with my values and interests": "Values alignment",
    "Previous experience or exposure": "Prior experience",
    "Related to my natural skills and abilities": "Natural strengths"
}

help_needed_col = ["#", 'Resume or LinkedIn help',
 'Interview prep and mock interviews',
 'Career coaching or mentorship',
 'Budgeting, money management and investing',
 'Emotional or mental health support',
 'Time management strategies',
 'Networking',
 'Professional attire']

help_needed_map = {
    "#": "#",
    "Resume or LinkedIn help": "Resume/LinkedIn",
    "Interview prep and mock interviews": "Interview prep",
    "Career coaching or mentorship": "Coaching/Mentorship",
    "Budgeting, money management and investing": "Financial help",
    "Emotional or mental health support": "Mental health",
    "Time management strategies": "Time mgmt",
    "Networking": "Networking",
    "Professional attire": "Attire"
}

score_card = ['I can manage challenges without giving up',
 'Stressed or overwhelmed',
 'Communicating professionally (verbal and written)',
 'Motivated to work toward your goals',
 'Focused and productive',
 'Creating a personal budget',
 'Understanding credit and credit scores',
 'I know how to present myself professionally in different settings']

entry_standardization_mapping = {
    # 'I can manage challenges without giving up' and 'I know how to present myself professionally in different settings'
    'Strongly disagree': 'Not at all',
    'Disagree': 'Slightly',
    'Neutral ': 'Moderately', # Keep the space here if it exists in your data
    'Neutral': 'Moderately',  # Add without space in case
    'Agree': 'Very',
    'Strongly agree': 'Extremely',

    # 'Stressed or overwhelmed', 'Motivated to work toward your goals', 'Focused and productive'
    'Never': 'Not at all',
    'Rarely': 'Slightly',
    'Sometimes': 'Moderately',
    'Often': 'Very',
    'Very Often': 'Extremely',

    # 'Communicating professionally (verbal and written)', 'Creating a personal budget', 'Understanding credit and credit scores'
    'Not confident': 'Not at all',
    'Not familiar': 'Not at all',
    'Slightly ': 'Slightly', # Keep the space here if it exists in your data
    'Slightly': 'Slightly', # Add without space in case
    'Somewhat': 'Moderately',
    'Very': 'Very',
    'Extremely': 'Extremely',
}

score_card_colname_name_mapping = {
    'Resilience': 'I can manage challenges without giving up',
    'Stress Level': 'Stressed or overwhelmed',
    'Communication': 'Communicating professionally (verbal and written)',
    'Motivation': 'Motivated to work toward your goals',
    'Focus & Productivity': 'Focused and productive',
    'Budgeting Skill': 'Creating a personal budget',
    'Credit Knowledge': 'Understanding credit and credit scores',
    'Professional Presence': 'I know how to present myself professionally in different settings'
}

skill_rating_map = {
    "Not at all": 1,
    "Slightly": 2,
    "Moderately": 3,
    "Very": 4,
    "Extremely": 5
}

# Apply mapping to all relevant columns
skill_cols = [
    "I can manage challenges without giving up",
    "Stressed or overwhelmed",
    "Communicating professionally (verbal and written)",
    "Motivated to work toward your goals",
    "Focused and productive",
    "Creating a personal budget",
    "Understanding credit and credit scores",
    "I know how to present myself professionally in different settings"
]

growth_questions = [
    "How confident are you now in managing your emotions and staying calm when things get stressful at work or in life?",
    "After learning about emotional intelligence, how are you at recognizing your personal emotional triggers?",
    "After the Communication Styles workshop, *how well do you understand your own communication style?*",
    "Are you more or less motivated about setting and actually reaching your goals after the goals workshop?",
    "What is your current clarity level about your possible career paths?",
    "How confident are you in your ability *to manage your money* this summer?",
    "After the personal branding session, how confident are you in *how you show up professionally*?",
    "Overall, how much do you feel you grew during the orientation?"
]

original_to_concise_question_names = {
    "How confident are you now in managing your emotions and staying calm when things get stressful at work or in life?": "Confidence in Managing Emotions",
    "After learning about emotional intelligence, how are you at recognizing your personal emotional triggers?": "Recognizing Emotional Triggers",
    "After the Communication Styles workshop, *how well do you understand your own communication style?*": "Understanding Communication Style",
    "Are you more or less motivated about setting and actually reaching your goals after the goals workshop?": "Motivation for Goal Setting",
    "What is your current clarity level about your possible career paths?": "Clarity on Career Paths",
    "How confident are you in your ability *to manage your money* this summer?": "Confidence in Money Management",
    "After the personal branding session, how confident are you in *how you show up professionally*?": "Confidence in Professional Presence",
    "Overall, how much do you feel you grew during the orientation?": "Overall Growth"
}

all_post_orientation_entry_mappings = {
    # Confidence in Managing Emotions
    'Extremely confident ': 'Highly Confident',
    'Very confident ': 'Very Confident',
    'A little confident ': 'Slightly Confident',
    'Not confident at all ': 'Not Confident At All',

    # Recognizing Emotional Triggers
    'A lot better, I understand them clearly now ': 'Significantly Better',
    'Much better ': 'Much Better',
    'Slightly better ': 'Slightly Better',
    'Not at all better ': 'Not Better At All',

    # Understanding Communication Style
    'I understand it clearly ': 'Clearly Understand',
    'I know it and I’m already working to improve it ': 'Understand & Improving',
    'I have a general idea ': 'General Understanding',
    'I still don’t really know it ': 'Do Not Understand',

    # Motivation for Goal Setting
    'Extremely motivated to take action now ': 'Highly Motivated',
    'Much more motivated ': 'Much More Motivated',
    'A little more motivated ': 'Slightly More Motivated',
    'Same ': 'No Change',
    'Less motivated ': 'Less Motivated',

    # Clarity on Career Paths
    'I feel very clear about my options and direction ': 'Very Clear',
    'I have solid ideas ': 'Solid Ideas',
    'I have a little more clarity now ': 'Slightly Clearer',
    'I still feel unsure ': 'Still Unsure',

    # Confidence in Money Management
    'Extremely confident ': 'Highly Confident',
    'Very confident ': 'Very Confident',
    'Somewhat confident ': 'Somewhat Confident',
    'Not confident at all ': 'Not Confident At All',

    # Confidence in Professional Presence
    'Extremely confident in how I present myself ': 'Highly Confident',
    'Very confident ': 'Very Confident',
    'Somewhat confident ': 'Somewhat Confident',
    'A little more confident ': 'Slightly More Confident',
    'Not confident yet ': 'Not Yet Confident',

    # Overall Growth During Orientation
    'More than expected': 'More Than Expected',
    'A lot ': 'Significant Growth',
    'Somewhat ': 'Some Growth',
    'A little bit ': 'Slight Growth',
    'Not at all ': 'No Growth At All'
}


all_post_orientation_score_map = {
    'Highly Confident': 4,
    'Very Confident': 4,
    'Somewhat Confident': 2,
    'Slightly Confident': 2,
    'Slightly More Confident': 1,
    'Not Confident At All': 0,
    'Not Yet Confident': 0,

    'Highly Motivated': 4,
    'Much More Motivated': 4,
    'Slightly More Motivated': 3,
    'No Change': 1,
    'Less Motivated': 0,

    'More Than Expected': 4,
    'Significant Growth': 4,
    'Some Growth': 3,
    'Slight Growth': 1,
    'No Growth At All': 0,

    'Significantly Better': 4,
    'Much Better': 4,
    'Slightly Better': 3,
    'Not Better At All': 1,

    'Clearly Understand': 4,
    'Understand & Improving': 4,
    'General Understanding': 3,
    'Do Not Understand': 1,

    'Very Clear': 4,
    'Solid Ideas': 3,
    'Slightly Clearer': 2,
    'Still Unsure': 1
}
