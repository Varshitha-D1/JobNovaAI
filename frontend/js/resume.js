document
.getElementById("analyzeBtn")
.addEventListener("click", async () => {

    const fileInput =
        document.getElementById("resumeFile");

    const file =
        fileInput.files[0];

    if (!file) {

        alert("Please select a PDF resume.");

        return;
    }

    document
        .getElementById("loading")
        .style.display = "block";

    const jobDescription =
        document.getElementById(
            "jobDescription"
        ).value;

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    formData.append(
        "job_description",
        jobDescription
    );

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/analyze_resume",
                {
                    method: "POST",
                    body: formData
                }
            );

        const data =
            await response.json();

        document
            .getElementById("result")
            .innerHTML = `

                <h3>AI Resume Summary</h3>
                <div>
                    ${data.summary.replace(/\n/g, "<br>")}
                </div>

                <hr>

                <h3>Skill Gap Analysis</h3>
                <div>
                    ${data.skill_gap.replace(/\n/g, "<br>")}
                </div>

                <hr>

                <h3>Interview Questions</h3>
                <div>
                    ${data.questions.replace(/\n/g, "<br>")}
                </div>

                <hr>

                <h3>Hire Recommendation</h3>
                <div>
                    ${data.hire.replace(/\n/g, "<br>")}
                </div>

                <hr>

                <h3>Reject Recommendation</h3>
                <div>
                    ${data.reject.replace(/\n/g, "<br>")}
                </div>

                <hr>

                <h3>Judge Verdict</h3>
                <div>
                    ${data.judge.replace(/\n/g, "<br>")}
                </div>

            `;

    } catch (error) {

        document
            .getElementById("result")
            .innerHTML = `
                <h3>Error</h3>
                <p>Unable to analyze resume.</p>
            `;

        console.error(error);
    }

    document
        .getElementById("loading")
        .style.display = "none";

});