const text = document.getElementById("text");
const counter = document.getElementById("counter");
const clearBtn = document.getElementById("clearBtn");

function updateCounter() {
  counter.textContent = `${text.value.length} characters`;
}

text.addEventListener("input", updateCounter);
clearBtn.addEventListener("click", () => {
  text.value = "";
  text.focus();
  updateCounter();
});

updateCounter();
