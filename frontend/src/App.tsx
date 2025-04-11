import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import { Map, Navigation } from "lucide-react";
import HeatMapView from "./views/HeatMapView";
import TableView from "./views/TableView";

function App() {
  return (
    <BrowserRouter>
      <div className="flex flex-col min-h-screen bg-gray-100">
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<HeatMapView />} />
            <Route path="/table" element={<TableView />} />
          </Routes>
        </main>

        <nav className="fixed bottom-0 w-full bg-white border-t border-gray-200 shadow-lg">
          <div className="flex justify-around py-4">
            <Link
              to="/"
              className="flex flex-col items-center text-gray-600 hover:text-blue-600 transition-colors"
            >
              <Map size={28} className="mb-1" />
              <span className="text-sm font-medium">מפה</span>
            </Link>
            <Link
              to="/table"
              className="flex flex-col items-center text-gray-600 hover:text-blue-600 transition-colors"
            >
              <Navigation size={28} className="mb-1" />
              <span className="text-sm font-medium">נְתוּנִים</span>
            </Link>
          </div>
        </nav>
      </div>
    </BrowserRouter>
  );
}

export default App;
