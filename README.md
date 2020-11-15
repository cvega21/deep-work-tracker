<h1>Toggl API - Deep Work Tracker</h1>
<p> Deep Work is defined by author Cal Newport as “Professional activity performed in a state of distraction-free concentration that push your cognitive capabilities to their limit". This script defines deep work as a function of consecutive time spent on a tracked task - by default, if a task was tracked for >60 minutes, it is classified as deep work. </p>

<h3>API</h3>
<p>Built on top of Toggl's API. Documentation found <a href="https://github.com/toggl/toggl_api_docs">here.</a></p>

<h3>Installation</h3>
<ul>
  <li>pip install requests</li>
  <li>change config API_TOKEN to your own Toggl API Token</li>
  <li>python run.py</li>
</ul>

<h3>Expected Output Example</h3>
<p>Time Period: 2020-11-01 to 2020-11-07</p>
<p>Deep Work threshold set at: 60 mins.</p>
<p>You logged a total of 10.0 deep work hours.</p> 
<p>You logged a total of 20.00 work hours.</p>
<p>Deep work made up 50.00% of your total work.</p>


<h3>License</h3>
<p>Copyright (c) 2020, Christian Vega-Munguia. MIT License</p>
