import { useEffect, useState } from "react";
import { format } from "date-fns";
import { ru } from "date-fns/locale";

// Тип для элемента данных
interface Dropping {
  id: number;
  coordinates: [number, number]; // Массив с двумя числами (широта, долгота)
  timestamp: string; // Временная метка в формате строки
}

function TableView() {
  const [data, setData] = useState<Dropping[]>([]); // Указываем тип данных

  useEffect(() => {
    async function fetchData() {
      try {
        // Изменено на новый эндпоинт
        const response = await fetch("http://127.0.0.1:8000/fetch/droppings");
        const result: Dropping[] = await response.json(); // Ожидаем результат типа Dropping[]

        // Сортируем по времени (новые сверху)
        const sorted = result.sort(
          (a, b) =>
            new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()
        );

        setData(sorted);
      } catch (error) {
        console.error("Ошибка при получении данных:", error);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="p-4 pb-20">
      <h1 className="text-2xl font-bold mb-4">היסטוריה של ממצאים</h1>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white shadow-md rounded-lg">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-s font-medium text-gray-500 uppercase">
                תַאֲרִיך
              </th>
              <th className="px-6 py-3 text-left text-s font-medium text-gray-500 uppercase">
                קואורדינטות
              </th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {data.map((item) => (
              <tr key={item.id}>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {format(new Date(item.timestamp), "Pp", { locale: ru })}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-blue-500 underline">
                  <a
                    href={`https://www.google.com/maps?q=${item.coordinates[0]},${item.coordinates[1]}`}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {item.coordinates[0].toFixed(4)},{" "}
                    {item.coordinates[1].toFixed(4)}
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default TableView;
