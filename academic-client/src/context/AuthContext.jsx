import { createContext, useContext, useState } from "react";
import { saveAuth, getAuth, clearAuth } from "../services/authStorage";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(getAuth());

  const login = (data) => {
    const authData = {
      token: data.access_token,
      role: data.role,
      username: data.username,
    };

    saveAuth(authData);
    setUser(authData);
  };

  const logout = () => {
    clearAuth();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
