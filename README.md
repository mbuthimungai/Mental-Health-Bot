# Mental-Health-Bot
This is a bot that tracks mental health cases in social media platforms


%%{init: {'theme': 'default'}}%%
usecaseDiagram
  actor SocialMediaUser as "Social Media User"
  actor SystemAdmin as "System Administrator"
  actor HealthcareProfessional as "Healthcare Professional"
  actor GeneralPublic as "General Public/User"
  rectangle System {
    SocialMediaUser --> (Collect Data)
    SystemAdmin --> (Configure Bot)
    (Generate Insights) .> (View Insights) : <<include>>
    (Analyze Data) .> (Generate Insights) : <<include>>
    (Process Data) .> (Analyze Data) : <<include>>
    (Collect Data) .> (Process Data) : <<include>>
    HealthcareProfessional --> (View Insights)
    GeneralPublic --> (View Insights)
  }

