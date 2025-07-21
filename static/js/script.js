document.querySelectorAll('.nav-item.dropdown > a').forEach((dropdownToggle) => {
  dropdownToggle.addEventListener('click', function (e) {
    e.preventDefault(); // Prevent default link behavior
    const dropdownMenu = this.nextElementSibling;

    // Toggle current dropdown
    dropdownMenu.classList.toggle('show');
  });

});
const signUpButton = document.getElementById('signUp');

const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
  container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
  container.classList.remove('right-panel-active');
});
document.querySelectorAll(".toggle-password").forEach(icon => {
  icon.addEventListener("click", () => {
    const passwordInput = icon.previousElementSibling;
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      icon.classList.remove("fa-eye");
      icon.classList.add("fa-eye-slash");
    } else {
      passwordInput.type = "password";
      icon.classList.remove("fa-eye-slash");
      icon.classList.add("fa-eye");
    }
  });
});
// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", () => {
  const signUpForm = document.querySelector(".sign-up-container form");
  const signInForm = document.querySelector(".sign-in-container form");

  // Email regex pattern
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function validateForm(form) {
    const category = form.querySelector('select[name="role"]');
    const email = form.querySelector('input[type="email"]');
    const password = form.querySelector('input[type="password"]');

    // Trim values
    const emailVal = email.value.trim();
    const passwordVal = password.value.trim();
    const categoryVal = category.value;

    // Validation checks
    if (!categoryVal) {
      alert("Please select a category.");
      return false;
    }

    if (!emailVal || !emailPattern.test(emailVal)) {
      alert("Please enter a valid email address.");
      return false;
    }

    if (!passwordVal || passwordVal.length < 6) {
      alert("Password must be at least 6 characters long.");
      return false;
    }

    return true;
  }

  // Handle Sign Up form
  signUpForm.addEventListener("submit", function (e) {
    // e.preventDefault();
    if (!validateForm(this)) {
      e.preventDefault();
      alert("Sign Up successful!");
      
      
    
      // You can now proceed with form submission (e.g., send data to server)
      // this.submit();
    }
  });

  // Handle Sign In form
  signInForm.addEventListener("submit", function (e) {
    e.preventDefault();
    if (validateForm(this)) {
      alert("Sign In successful!");
      // this.submit();
    }
  });
});


