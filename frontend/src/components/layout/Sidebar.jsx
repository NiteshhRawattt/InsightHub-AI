import {
    MessageSquare,
    FileText,
    Star,
    History,
    Settings,
    Plus,
    User
} from "lucide-react";
function Sidebar() {
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