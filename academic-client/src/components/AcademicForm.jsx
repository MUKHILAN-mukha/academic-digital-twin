import { useState } from "react";

function AcademicForm({ onEventCreate }) {
  const [formData, setFormData] = useState({
    student_id: "",
    subject: "",
    attendance: false,
    homework_completion: 0,
    test_score: "",
    max_score: "",
    behavior_score: 0.5,
  });

  const [error, setError] = useState("");

  const validate = () => {
    if (!formData.student_id.trim()) return "Student ID is required";
    if (!formData.subject) return "Subject is required";
    if (formData.test_score < 0) return "Invalid test score";
    if (formData.max_score <= 0) return "Invalid max score";
    if (+formData.test_score > +formData.max_score)
      return "Test score cannot exceed max score";
    return "";
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const err = validate();
    if (err) {
      setError(err);
      return;
    }
    setError("");
    onEventCreate(formData);
  };

  return (
    <div className="w-full max-w-4xl bg-white rounded-2xl shadow-xl">
      {/* Header */}
      <div className="px-8 py-6 border-b bg-slate-50 rounded-t-2xl">
        <h2 className="text-xl font-semibold">Academic Data Entry</h2>
        <p className="text-sm text-slate-500">
          Enter student academic information and performance metrics
        </p>
      </div>

      {/* Form */}
      <form onSubmit={handleSubmit} className="p-8 space-y-6">
        {error && (
          <div className="text-red-600 text-sm font-medium">{error}</div>
        )}

        {/* Student ID */}
        <div>
          <label className="text-sm font-medium">
            Student ID <span className="text-red-500">*</span>
          </label>
          <input
            className="mt-1 w-full rounded-lg bg-slate-100 px-4 py-2 outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Enter student ID"
            value={formData.student_id}
            onChange={(e) =>
              setFormData({ ...formData, student_id: e.target.value })
            }
          />
        </div>

        {/* Grid */}
        <div className="grid grid-cols-2 gap-6">
          {/* Homework */}
          <div>
            <label className="text-sm font-medium">
              Today's Homework Completion (%)
            </label>
            <input
              type="number"
              className="mt-1 w-full rounded-lg bg-slate-100 px-4 py-2"
              value={formData.homework_completion}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  homework_completion: e.target.value,
                })
              }
            />
          </div>

          {/* Max Score */}
          <div>
            <label className="text-sm font-medium">Max Score</label>
            <input
              type="number"
              className="mt-1 w-full rounded-lg bg-slate-100 px-4 py-2"
              placeholder="e.g. 100"
              value={formData.max_score}
              onChange={(e) =>
                setFormData({ ...formData, max_score: e.target.value })
              }
            />
          </div>

          {/* Subject */}
          <div>
            <label className="text-sm font-medium">Subject</label>
            <select
              className="mt-1 w-full rounded-lg bg-slate-100 px-4 py-2"
              onChange={(e) =>
                setFormData({ ...formData, subject: e.target.value })
              }
            >
              <option value="">Select subject</option>
              <option>Math</option>
              <option>Science</option>
              <option>English</option>
            </select>
          </div>

          {/* Attendance */}
          <div className="flex items-center gap-3 mt-6">
            <input
              type="checkbox"
              checked={formData.attendance}
              onChange={(e) =>
                setFormData({ ...formData, attendance: e.target.checked })
              }
            />
            <span className="font-medium">Present</span>
          </div>

          {/* Test Score */}
          <div>
            <label className="text-sm font-medium">Test Score</label>
            <input
              type="number"
              className="mt-1 w-full rounded-lg bg-slate-100 px-4 py-2"
              placeholder="Enter test score"
              value={formData.test_score}
              onChange={(e) =>
                setFormData({ ...formData, test_score: e.target.value })
              }
            />
          </div>

          {/* Behavior */}
          <div>
            <label className="text-sm font-medium">Behavior</label>
            <input
              className="mt-1 w-full rounded-lg bg-slate-100 px-4 py-2"
              placeholder="e.g. Excellent, Good, Fair"
            />
          </div>
        </div>

        {/* Slider */}
        <div>
          <div className="flex justify-between items-center mb-2">
            <label className="text-sm font-medium">Score (0–1)</label>
            <span className="text-sm bg-blue-100 text-blue-600 px-3 py-1 rounded-full">
              {formData.behavior_score.toFixed(2)}
            </span>
          </div>
          <input
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={formData.behavior_score}
            onChange={(e) =>
              setFormData({
                ...formData,
                behavior_score: Number(e.target.value),
              })
            }
            className="w-full"
          />
        </div>

        {/* Submit */}
        <button
          type="submit"
          className="w-full mt-4 py-3 rounded-xl text-white font-semibold
                     bg-gradient-to-r from-blue-500 to-indigo-600
                     hover:opacity-90 transition"
        >
          Create Academic Event
        </button>
      </form>
    </div>
  );
}

export default AcademicForm;
