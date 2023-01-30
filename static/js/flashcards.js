/*
 *   Copyright (c) 2023 Jack Bennett
 *   All rights reserved.
 *
 *   Please see the LICENCE file for more information.
 */

document.addEventListener("DOMContentLoaded", () => {
    // cardset import submit event
    let importForm = document.querySelector("#setid-prompt form");

    importForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const data = new FormData(importForm);
        console.log(data);

        fetch("/flashcards", {
            method: "POST",
            body: data
        }).then((response) => {
            if (response.status == 200) {
                window.location.reload();
            }
        })
    });
});
