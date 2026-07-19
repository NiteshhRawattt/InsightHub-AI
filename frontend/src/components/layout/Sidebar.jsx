import {
    MessageSquare,
    FileText,
    Star,
    History,
    Settings,
    Plus,
    User
} from "lucide-react";
import { useEffect, useRef, useState } from "react";

function Sidebar({
    selectedDocument,
    setSelectedDocument,
})  {
    const fileInputRef = useRef(null);
    const [documents, setDocuments] = useState([]);
    const handleFileUpload = async (event) => {
        const file = event.target.files[0];

        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch(
                "http://localhost:8000/api/v1/upload/",
                {
                    method: "POST",
                    body: formData,
                }
            );

            const data = await response.json();

            alert(data.message);

            event.target.value = "";
        } catch (error) {
            console.error(error);
            alert("Upload failed!");
        }
    };

    useEffect(() => {
        const fetchDocuments = async () => {
            try {
                const response = await fetch(
                    "http://localhost:8000/api/v1/upload/files"
                );

                const data = await response.json();

                setDocuments(data.files);
            } catch (error) {
                console.error("Failed to fetch documents:", error);
            }
        };

        fetchDocuments();   
    }, []);

    return (
        <div className="w-72 bg-surface-800 border-r border-surface-500 flex flex-col">

            {/* Logo */}
            <div className="p-5">
                <h1 className="text-2xl font-bold text-brand-400">
                    InsightHub AI
                </h1>

                <button className="btn-primary w-full mt-8">
                    <Plus size={18} />
                    New Chat
                </button>
            </div>

            {/* Menu */}
            <div className="flex-1 px-4 space-y-2">

                <div className="sidebar-item active">
                    <MessageSquare size={18} />
                    <span>Research Chat</span>
                </div>

                <div className="sidebar-item">
                    <FileText size={18} />
                    <span>Documents</span>
                </div>

                {selectedDocument && (
                    <p className="text-xs text-brand-400 px-3 mt-2">
                    Active: {selectedDocument}
                    </p>
                    )}

                {documents.length > 0 && (
                    <div className="mt-2 mb-3 space-y-2">   
                        {documents.map((doc, index) => (
                            <div
                                key={index}
                                 onClick={() => setSelectedDocument(doc)}
                                className={`flex items-center gap-2 px-3 py-2 text-sm rounded-lg cursor-pointer transition

                                ${
                                    selectedDocument === doc
                                    ? "bg-brand-500 text-white"
                                    :"text-gray-300 hover:bg-surface-700"
                                }`}
                            >
                                <FileText size={16} />
                                <span className="truncate">{doc}</span>
                            </div>
                        ))}
                    </div>
                )}

                <input
                    type="file"
                    accept=".pdf"
                    ref={fileInputRef}
                    className="hidden"
                    onChange={handleFileUpload}
                />

                <button
                    className="btn-primary w-full mt-2"
                    onClick={() => fileInputRef.current.click()}
                >
                 <Plus size={18} />
                 Upload PDF
                </button>

                <div className="sidebar-item">
                    <Star size={18} />
                    <span>Favorites</span>
                </div>

                <div className="sidebar-item">
                    <History size={18} />
                    <span>History</span>
                </div>

                <div className="sidebar-item">
                    <Settings size={18} />
                    <span>Settings</span>
                </div>

            </div>

            {/* User */}
            <div className="p-5 border-t border-surface-500">
                <div className="sidebar-item">
                    <User size={18} />
                    <span>Nitesh Rawat</span>
                </div>
            </div>

        </div>
    );
}

export default Sidebar;