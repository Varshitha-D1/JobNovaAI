document
.getElementById("generateRoadmapBtn")
.addEventListener("click", async () => {

    const careerGoal =
        document.getElementById(
            "careerGoal"
        ).value;

    document
    .getElementById("result")
    .innerHTML = `
        <div class="loading-box" style="display:block;">

            <div class="loader"></div>

            <h3>🤖 AI is generating your roadmap...</h3>

            <p>
                Please wait a few seconds...
            </p>

        </div>
    `;

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/skill_navigator",
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                        "application/json"
                    },
                    body: JSON.stringify({
                        career_goal:
                        careerGoal
                    })
                }
            );

        const data =
            await response.json();

        document
        .getElementById("result")
        .innerHTML = `
            <div style="white-space: pre-wrap;">
                ${data.roadmap}
            </div>
        `;

    } catch (error) {

        document
        .getElementById("result")
        .innerHTML =
        "Unable to generate roadmap.";

        console.error(error);
    }

});