# Filters

file okf_xml@ysc-key-based-wc.fprm
:

<?xml version="1.0" encoding="UTF-8" standalone="no"?><its:rules xmlns:its="http://www.w3.org/2005/11/its" xmlns:itsx="http://www.w3.org/2008/12/its-extensions" xmlns:okp="okapi-framework:xmlfilter-options" xmlns:xlink="http://www.w3.org/1999/xlink" its:translate="no" version="1.0">

<!-- 

    This filter is used to obtain wordcounts of parts of files or projects. 
    Insert the rules in the only filtering rule with translate="yes" below, like so
    //data[not(@type) and not(starts-with(@name, '&gt;'))][ << insert condition here >> ]/value

  -->
  
 <its:translateRule selector="/root" translate="no"/>
 <its:translateRule itsx:idValue="../@name" selector="//data[not(@type) and not(starts-with(@name, '&gt;'))][@name[starts-with(., 'SurveyCategoryOptions.LeadershipStylesQuestionnaire.Instrument.Instructions') or starts-with(., 'LeadershipStylesQuestionnaire.SurveyName') or starts-with(., 'SurveyCategories.LeadershipStylesQuestionnaire') or starts-with(., 'Label.Survey.PsychometricTest') or starts-with(., 'Label.Survey.General')]]/value" translate="yes"/>
 <its:translateRule itsx:idValue="../@name" selector="//data[starts-with(@name, 'SurveyQuestions.CognitiveAbilityTest.QuestionInstructions.Num_0')]/value" translate="no"/>
 <its:translateRule selector="//data[@mimetype]/value" translate="no"/>
 <its:translateRule selector="//data[substring(@name, string-length(@name) - string-length('.FieldName')+1)='.FieldName']/value" translate="no"/>

 <!-- inline HTML --> 
 <its:withinTextRule selector="//sub|//sup|//img|//b|//i|//u|//span|//em|//strong" withinText="yes"/>




Code finder: 

```
<okp:codeFinder useCodeFinder="yes">#v1
count.i=4
rule0=\{\{[^}\n]+?\}\}
rule1=\{[^}\n]+?\}
rule2=\&lt;(/?)\w+[^&gt;]*?&gt;
rule3=\"(?![:,\n])([^\"]*?)\"(?=:)
</okp:codeFinder>
</its:rules>
```

---

# to match text units with a certain key:

\n\s+<data name=".*(app\.pageTitle\.participantsDashboard|app\.pageTitle\.yscqClientDashboard|app\.pageTitle\.yscqDashboard|dashboard\.aggregatedSummary\.no|dashboard\.aggregatedSummary\.placeholder|dashboard\.aggregatedSummaryComponent|dashboard\.barChartNoDataPlaceholder\.resultsTooNarrow|dashboard\.clientGoalForm|dashboard\.createClient|dashboard\.createDevelopmentGoalContainer|dashboard\.createDevelopmentGoalForm|dashboard\.createDevelopmentGoalPulseForm|dashboard\.createExperiencesForm|dashboard\.cultureBarChart|dashboard\.customIndividual|dashboard\.dashboardFeedback|dashboard\.dashboardGoal|dashboard\.dashboardPlaceholder|dashboard\.dashboardShareButton|dashboard\.development|dashboard\.edit|dashboard\.executive|dashboard\.explore|dashboard\.(indiv|man|not|organ|overall|pageTitle|personal|potential|recomm|score|sidebar|team|update|view)|edpTest\.pageTitle\.participantsDashboard|feedback\.feedbackResponded\.viewDashboard|feedback\.sharedDashboard|finder\.finderContainer\.button\.viewTeamDashboard|global\.dashboard|global\.feedbackTabs\.sharedDashboards|lsqParticipantReport|app\.participantReport\.(name|date|jobTitle|how|leaders|know)|global\.(lsq|report|judgment|drive|influence)|app\.[b-n]|app\.pageTitle\.[a-nv]|app\.pageTitle\.(?!yscqClientDashboard|yscqDashboard|participantsDashboard)|app\.[s-z]|baseLineChart|clientPeople\.|clients\.[cu]|edpParticipant|edpTest\.[c-s](?!ageTitle\.participantsDash)|(?<!Stakeholder)feedback\.[apru]|feedback\.feedback(?!Responded\.viewDashboard)|feedbackLine|finder\.finder(?!Container\.button)|finder.(fit|pag)|global.[abc]|global\.d(?!ashboard|rive)|global\.[ef](?!eedbackTabs\.sharedDashboards)|global\.[ghi](?!nfluence)|global\.[j-z](?!sqReport|eport|udgment)|profilesOfSuccess\.(pageTitle|profiles?OfSuccess)|project\.[a-z]|shared\.|(?<!Error\.)surveys\.|tasks\.a|team\.(pageTitle|team)|teamDynamicsLineChart\.p|(?<!Error\.)Demographics\.(Age|CurrentLength|Disability|EthnicOrigin|Gender|Industry|Job|Language|Last|Level|Location|Sexual|Transgender)|app.clientUser|app.demo|clientPeople.userDemo).*" [^>]+>[\n\s]+<value>[\s\S]*?</value>[\n\s]+</data>



\n\s+<trans-unit id=".*(app\.pageTitle\.participantsDashboard|app\.pageTitle\.yscqClientDashboard|app\.pageTitle\.yscqDashboard|dashboard\.aggregatedSummary\.no|dashboard\.aggregatedSummary\.placeholder|dashboard\.aggregatedSummaryComponent|dashboard\.barChartNoDataPlaceholder\.resultsTooNarrow|dashboard\.clientGoalForm|dashboard\.createClient|dashboard\.createDevelopmentGoalContainer|dashboard\.createDevelopmentGoalForm|dashboard\.createDevelopmentGoalPulseForm|dashboard\.createExperiencesForm|dashboard\.cultureBarChart|dashboard\.customIndividual|dashboard\.dashboardFeedback|dashboard\.dashboardGoal|dashboard\.dashboardPlaceholder|dashboard\.dashboardShareButton|dashboard\.development|dashboard\.edit|dashboard\.executive|dashboard\.explore|dashboard\.(indiv|man|not|organ|overall|pageTitle|personal|potential|recomm|score|sidebar|team|update|view)|edpTest\.pageTitle\.participantsDashboard|feedback\.feedbackResponded\.viewDashboard|feedback\.sharedDashboard|finder\.finderContainer\.button\.viewTeamDashboard|global\.dashboard|global\.feedbackTabs\.sharedDashboards|lsqParticipantReport|app\.participantReport\.(name|date|jobTitle|how|leaders|know)|global\.(lsq|report|judgment|drive|influence)|app\.[b-n]|app\.pageTitle\.[a-nv]|app\.pageTitle\.(?!yscqClientDashboard|yscqDashboard|participantsDashboard)|app\.[s-z]|baseLineChart|clientPeople\.|clients\.[cu]|edpParticipant|edpTest\.[c-s](?!ageTitle\.participantsDash)|(?<!Stakeholder)feedback\.[apru]|feedback\.feedback(?!Responded\.viewDashboard)|feedbackLine|finder\.finder(?!Container\.button)|finder.(fit|pag)|global.[abc]|global\.d(?!ashboard|rive)|global\.[ef](?!eedbackTabs\.sharedDashboards)|global\.[ghi](?!nfluence)|global\.[j-z](?!sqReport|eport|udgment)|profilesOfSuccess\.(pageTitle|profiles?OfSuccess)|project\.[a-z]|shared\.|(?<!Error\.)surveys\.|tasks\.a|team\.(pageTitle|team)|teamDynamicsLineChart\.p|(?<!Error\.)Demographics\.(Age|CurrentLength|Disability|EthnicOrigin|Gender|Industry|Job|Language|Last|Level|Location|Sexual|Transgender)|app.clientUser|app.demo|clientPeople.userDemo)[^"]*"[^>]*>[\n\s]+<source>[\s\S]*?</source>[\n\s]+</trans-unit>

----

