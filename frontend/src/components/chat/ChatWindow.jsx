function ChatWindow() {
    return (
        <div className="flex-1 flex items-center justify-center px-8">

            <div className="max-w-2xl text-center">

                <h1 className="text-5xl font-bold text-white">
                    Welcome to InsightHub AI
                </h1>

                <p className="mt-6 text-lg text-gray-400">
                    Your AI-powered research assistant.
                </p>

                <p className="mt-2 text-gray-500">
                    Upload PDFs, ask questions, summarize documents and discover insights.
                </p>
                <div className="mt-12">
                    <h2 className="text-lg font-semibold text-gray-300 mb-4">
                        Suggested Prompts
                    </h2>

                    <div className="grid grid-cols-2 gap-4">

                        <div className="glass-card p-4 cursor-pointer hover:border-brand-500 transition-all">
                            Summarize this document
                        </div>

                        <div className="glass-card p-4 cursor-pointer hover:border-brand-500 transition-all">
                            Explain Machine Learning
                        </div>

                        <div className="glass-card p-4 cursor-pointer hover:border-brand-500 transition-all">
                            Compare CNN vs Transformer
                        </div>

                        <div className="glass-card p-4 cursor-pointer hover:border-brand-500 transition-all">
                            Generate Interview Questions
                        </div>

                    </div>
                </div>

            </div>

        </div>
    );
}

export default ChatWindow;