import { useEffect, useState } from "react";
import { MapContainer, TileLayer, Circle } from "react-leaflet";
import "leaflet/dist/leaflet.css";

// Тип для координат
interface Coordinates {
  [key: string]: [number, number]; // Объект, где ключ — это строка (ID), а значение — массив с двумя числами (широта, долгота)
}

function HeatMapView() {
  const [coordinates, setCoordinates] = useState<Coordinates>({}); // Указываем тип для coordinates

  useEffect(() => {
    async function fetchCoordinates() {
      try {
        const response = await fetch("http://127.0.0.1:8000/fetch/mapcords"); // Запрос на ваш эндпоинт
        const result = await response.json();
        setCoordinates(result); // Получаем данные и сохраняем в state
      } catch (error) {
        console.error("Ошибка при получении данных:", error);
      }
    }

    fetchCoordinates();
  }, []);

  return (
    <div className="h-[calc(100vh-5rem)]">
      <MapContainer
        center={[31.25181, 34.7913]} // Центр Беэр-Шевы
        zoom={15}
        className="h-full w-full"
      >
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        {Object.entries(coordinates).map(([id, coord]) => (
          <Circle
            key={id}
            center={coord} // Координаты из API
            radius={50}
            pathOptions={{
              color: "red",
              fillColor: "red",
            }}
          />
        ))}
      </MapContainer>
    </div>
  );
}

export default HeatMapView;
