type NavbarProps = {
  text: string;
  onClick: () => void;
};

function Navbar({ text, onClick }: NavbarProps) {
  return (
    <div
      style={{
        width: "100%",
        height: "60px",
        backgroundColor: "#4c2004",
        background: "linear-gradient(to right, #4c2004, #65351f)",
      }}
    ></div>
  );
}
