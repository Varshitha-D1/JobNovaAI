document
.getElementById("startInterviewBtn")
.addEventListener("click", async () => {

    const file =
        document.getElementById(
            "resumeFile"
        ).files[0];

    const jobDescription =
        document.getElementById(
            "jobDescription"
        ).value;

    if (!file) {

        alert("Please upload resume.");

        return;
    }

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

    document
    .getElementById("result")
    .innerHTML = `
        <div class="loading-box" style="display:block;">

            <div class="loader"></div>

            <h3>🎤 Generating Interview Questions...</h3>

            <p>
                AI is preparing personalized questions.
            </p>

        </div>
    `;

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

                <h2>Interview Questions</h2>

                <div style="white-space: pre-wrap;">
                    ${data.questions}
                </div>

            `;

    } catch (error) {

        document
            .getElementById("result")
            .innerHTML =
            "Unable to generate questions.";

        console.error(error);
    }

});