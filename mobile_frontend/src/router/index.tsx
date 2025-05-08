import { createBrowserRouter } from "react-router-dom";
import Login from '@/pages/login'
import Home from '@/pages/home'
import ProtectedRoute from "./protectedRouter";
const router = createBrowserRouter([
    { path: '/', element: <Login /> },
    {
        path: "/home",
        element: (
          <ProtectedRoute>
            <Home />
          </ProtectedRoute>
        ),
      },
])

export default router