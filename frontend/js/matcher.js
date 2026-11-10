document
.getElementById("matchBtn")
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

        alert("Upload Resume");

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

            <h3>🎯 Matching Resume...</h3>

            <p>
                AI is comparing your resume with the job description.
            </p>

        </div>
    `;

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/company_match",
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
                    <h2>Match Score</h2>
                    
                <h1>${data.score}%</h1>

                <h3>Reason</h3>

                <p>${data.reason}</p>

            `;

    } catch (error) {

        document
            .getElementById("result")
            .innerHTML =
            "Unable to match resume.";

        console.error(error);
    }

});