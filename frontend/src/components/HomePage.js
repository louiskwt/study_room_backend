import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPage from "./RoomJoinPage";

const HomePage = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<RoomJoinPage />} />
        <Route path="/create" element={<CreateRoomPage />} />
        <Route path="/join" element={<RoomJoinPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default HomePage;
