<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles_result.css') }}">
    <title>Pie Charts</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>

    <div class="main-div">
        <h2 class="headtext">РЕЗУЛЬТАТИ ОПИТУВАННЯ</h2>
    
        <div class="ask-div">
            <img src="{{ urls[0] }}" alt="Image">
            <canvas id="diagram-0" class="diagram"></canvas>
            <button type="button" class='mark-button' disabled="true">{{avgMark[0]}}</button>
        </div>
    
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                const canvas = document.getElementById("diagram-0");
                const ctx = canvas.getContext("2d");
                const data = {{ percentages_data }};
                const canvasWidth = canvas.width;
                const canvasHeight = canvas.height;
    
                // Calculate the total sum of values
                const totalSum = Object.values(data[1]).reduce((a, b) => a + b, 0);
    
                // Calculate the width of each section based on the values
                const sectionWidths = {};
                for (const key in data[1]) {
                    const value = data[1][key];
                    const widthPercentage = (value / totalSum) * 100;
                    sectionWidths[key] = (canvasWidth * widthPercentage) / 100;
                }
    
                // Set the colors for each section
                const sectionColors = {
                    1: "red",
                    2: "green",
                    3: "blue",
                    4: "yellow",
                    5: "orange"
                };
    
                // Draw the diagram sections
                let startX = 0;
                for (const key in sectionWidths) {
                    const sectionWidth = sectionWidths[key];
                    const sectionColor = sectionColors[key];
    
                    // Set the style for the section
                    ctx.fillStyle = sectionColor;
    
                    // Draw the section
                    ctx.fillRect(startX, 0, sectionWidth, canvasHeight);
    
                    startX += sectionWidth;
                }
            });
        </script>
        <div class="ask-div">
            <img src="{{ urls[1] }}" alt="Image">
            <canvas id="diagram-1" class="diagram"></canvas>
            <button type="button" class='mark-button' disabled="true">{{avgMark[1]}}</button>
        </div>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                const canvas = document.getElementById("diagram-1");
                const ctx = canvas.getContext("2d");
                const data = {{ percentages_data }};
                const canvasWidth = canvas.width;
                const canvasHeight = canvas.height;
    
                // Calculate the total sum of values
                const totalSum = Object.values(data[2]).reduce((a, b) => a + b, 0);
    
                // Calculate the width of each section based on the values
                const sectionWidths = {};
                for (const key in data[2]) {
                    const value = data[2][key];
                    const widthPercentage = (value / totalSum) * 100;
                    sectionWidths[key] = (canvasWidth * widthPercentage) / 100;
                }
    
                // Set the colors for each section
                const sectionColors = {
                    1: "red",
                    2: "green",
                    3: "blue",
                    4: "yellow",
                    5: "orange"
                };
    
                // Draw the diagram sections
                let startX = 0;
                for (const key in sectionWidths) {
                    const sectionWidth = sectionWidths[key];
                    const sectionColor = sectionColors[key];
    
                    // Set the style for the section
                    ctx.fillStyle = sectionColor;
    
                    // Draw the section
                    ctx.fillRect(startX, 0, sectionWidth, canvasHeight);
    
                    startX += sectionWidth;
                }
            });
        </script>
    </div>
    
    

        
</body>
</html>
