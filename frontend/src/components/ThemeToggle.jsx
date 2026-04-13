function ThemeToggle() {
  const toggleTheme = () => {
    document.body.classList.toggle("dark");
  };

  return <button onClick={toggleTheme}>Toggle Theme</button>;
}

export default ThemeToggle;