import "./App.css";
import rectangle9 from "./assets/rectangle9.svg";
import rectangle7 from "./assets/rectangle7.svg";
import rectangle1 from "./assets/rectangle1.svg";
import rectangle8 from "./assets/rectangle8.svg";
import rectangle6 from "./assets/rectangle6.png";
const App = () => {
  return (
    <div className="container">
      <div className="container-1">
        <div className="container-2">
          <img className="image" src={rectangle6} />
          <span className="text">ALITO</span>
        </div>
        <div className="container-3">
          <span className="text-1">Campaigns</span>
        </div>
        <div className="container-4">
          <span className="text-2">Payouts</span>
        </div>
        <div className="container-5">
          <span className="text-3">Marketplace</span>
        </div>
        <div className="container-6">
          <span className="text-4">Profile</span>
        </div>
      </div>
      <div className="container-7">
        <span className="text-5">Data Collection</span>
      </div>
      <div className="container-8">
        <span className="text-6">Search by #tag</span>
        <span className="text-7">Search by FYP</span>
        <span className="text-8">Search by Parlay</span>
      </div>
      <div className="container-9">
        <span className="text-9">Generate Account Stats</span>
        <span className="text-10">Generate Video Stats</span>
      </div>
      <div className="container-10">
        <img className="image-1" src={rectangle8} />
        <img className="image-2" src={rectangle1} />
      </div>
      <div className="container-11">
        <img className="image-3" src={rectangle9} />
        <img className="image-4" src={rectangle7} />
      </div>
    </div>
  );
};
export default App;
