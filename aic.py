import tkinter as tk
from tkinter import messagebox
from typing import Optional
import random

import matplotlib.pyplot as plt
from owlready2 import Ontology, get_ontology
import numpy as np


def load_ontology(file_path: str) -> Optional[Ontology]:
    """
    Load the ontology from the given file path.
    """
    try:
        ontology = get_ontology(file_path).load()
        return ontology
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load ontology: {e}")
        return None


def list_subclasses(ontology: Ontology, parent_class_name: str) -> str:
    """
    List all subclasses under a specified parent class.
    """
    parent_class = ontology.search_one(iri=f"*{parent_class_name}")
    if not parent_class:
        return f"No shape named '{parent_class_name}' found."

    subclasses = [subclass.name for subclass in parent_class.subclasses()]
    if parent_class_name == "ThreeDimensionalShape":
        result = "List of three dimensional shapes"
    elif parent_class == "TwoDimensionalShape":
        result = "List of two dimensional shapes"
    else:
        result = "List of requested shapes"

    return f"{result}:\n" + "\n".join(f"  - {name}" for name in subclasses)


def search_shape(ontology: Ontology, shape_name: str, for_quiz: bool) -> str:
    """
    Search for a shape by name and display its details.
    """
    shape_name = shape_name.title()
    shape_class = ontology.search_one(iri=f"*{shape_name}")
    if not shape_class:
        return f"No shape named '{shape_name}' found."
    

    details = f"Details for shape '{shape_class.name}':\n\n"

    if for_quiz:
        details = ""        
    
    if hasattr(shape_class, "comment") and shape_class.comment.first():
        details += f"  Description: {shape_class.comment.first()}\n\n"

    if hasattr(shape_class, "area_formula") and shape_class.area_formula.first():
        details += f"  Area Formula: {shape_class.area_formula.first()}\n\n"

    if hasattr(shape_class, "perimeter_formula") and shape_class.perimeter_formula.first():
        details += f"  Perimeter Formula: {shape_class.perimeter_formula.first()}\n\n"

    if hasattr(shape_class, "volume_formula") and shape_class.volume_formula.first():
        details += f"  Volume Formula: {shape_class.volume_formula.first()}\n\n"
    return details

def visualize_shape(shape_name: str):
    """
    Visualize the specified shape using matplotlib.
    """
    try:
        if shape_name.lower() == "circle":
            fig, ax = plt.subplots()
            circle = plt.Circle((0.5, 0.5), 0.4, color="blue", fill=False, linewidth=2)
            ax.add_artist(circle)
            ax.set_aspect("equal", adjustable="datalim")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            plt.title("Circle")
            plt.show()

        elif shape_name.lower() == "square":
            fig, ax = plt.subplots()
            square = plt.Rectangle((0.1, 0.1), 0.8, 0.8, color="green", fill=False, linewidth=2)
            ax.add_artist(square)
            ax.set_aspect("equal", adjustable="datalim")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            plt.title("Square")
            plt.show()

        elif shape_name.lower() == "rectangle":
            fig, ax = plt.subplots()
            rectangle = plt.Rectangle((0.1, 0.3), 0.8, 0.4, color="orange", fill=False, linewidth=2)
            ax.add_artist(rectangle)
            ax.set_aspect("equal", adjustable="datalim")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            plt.title("Rectangle")
            plt.show()

        elif shape_name.lower() == "triangle":
            fig, ax = plt.subplots()
            triangle = plt.Polygon([[0.5, 0.8], [0.2, 0.2], [0.8, 0.2]], color="purple", fill=False, linewidth=2)
            ax.add_artist(triangle)
            ax.set_aspect("equal", adjustable="datalim")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            plt.title("Triangle")
            plt.show()

        elif shape_name.lower() == "rhombus":
            fig, ax = plt.subplots()
            rhombus = plt.Polygon([[0.5, 0.9], [0.8, 0.5], [0.5, 0.1], [0.2, 0.5]], color="red", fill=False, linewidth=2)
            ax.add_artist(rhombus)
            ax.set_aspect("equal", adjustable="datalim")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            plt.title("Rhombus")
            plt.show()

        elif shape_name.lower() == "parallelogram":
            fig, ax = plt.subplots()
            parallelogram = plt.Polygon([[0.2, 0.2], [0.5, 0.2], [0.8, 0.8], [0.5, 0.8]], color="cyan", fill=False, linewidth=2)
            ax.add_artist(parallelogram)
            ax.set_aspect("equal", adjustable="datalim")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis("off")
            plt.title("Parallelogram")
            plt.show()

        elif shape_name.lower() == "sphere":
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            u = np.linspace(0, 2 * np.pi, 100)
            v = np.linspace(0, np.pi, 100)
            x = np.outer(np.cos(u), np.sin(v))
            y = np.outer(np.sin(u), np.sin(v))
            z = np.outer(np.ones(np.size(u)), np.cos(v))
            ax.plot_wireframe(x, y, z, color="blue")
            ax.set_title("Sphere")
            plt.show()

        elif shape_name.lower() == "cylinder":
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            z = np.linspace(0, 1, 100)
            theta = np.linspace(0, 2 * np.pi, 100)
            theta_grid, z_grid = np.meshgrid(theta, z)
            x = np.cos(theta_grid)
            y = np.sin(theta_grid)
            ax.plot_wireframe(x, y, z_grid, color="green")
            ax.set_title("Cylinder")
            plt.show()

        elif shape_name.lower() == "cuboid" or shape_name.lower() == "cube":
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                               [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
            edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                     (4, 5), (5, 6), (6, 7), (7, 4),
                     (0, 4), (1, 5), (2, 6), (3, 7)]
            for edge in edges:
                ax.plot3D(*zip(points[edge[0]], points[edge[1]]), color="brown")
            ax.set_title("Cuboid")
            plt.show()

        elif shape_name.lower() == "cone":
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            z = np.linspace(0, 1, 50)
            theta = np.linspace(0, 2 * np.pi, 50)
            theta_grid, z_grid = np.meshgrid(theta, z)
            x = z_grid * np.cos(theta_grid)
            y = z_grid * np.sin(theta_grid)
            ax.plot_surface(x, y, z_grid, color="orange", alpha=0.6)
            ax.set_title("Cone")
            plt.show()

        else:
            messagebox.showinfo("Visualization", f"Visualization for '{shape_name}' is not yet implemented.")
    except Exception as e:
        messagebox.showerror("Visualization Error", f"Error visualizing shape: {e}")



class OntologyApp:
    def __init__(self, root: tk.Tk, ontology: Ontology):
        self.root = root
        self.ontology = ontology
        self.current_quiz_shape = None

        self.root.title("Intelligent Tutoring System - Geometry")
        self.root.geometry("700x550")

        # Title Label
        title_label = tk.Label(root, text="Intelligent Tutoring System - Geometry", font=("Arial", 16))
        title_label.pack(pady=10)

        # Button to List all shapes
        button_3d = tk.Button(root, text="List Available Shapes", command=self.show_all_shapes)
        button_3d.pack(pady=5)

        # Button to List Subclasses of ThreeDimensionalShape
        button_3d = tk.Button(root, text="List Three Dimensional Shapes", command=self.show_3d_subclasses)
        button_3d.pack(pady=5)

        # Button to List Subclasses of TwoDimensionalShape
        button_2d = tk.Button(root, text="List Two Dimensional Shapes", command=self.show_2d_subclasses)
        button_2d.pack(pady=5)

        # Search Field and Button
        search_frame = tk.Frame(root)
        search_frame.pack(pady=10)
        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        search_button = tk.Button(search_frame, text="Search Shape", command=self.search_shape_details)
        search_button.pack(side=tk.LEFT)

        # Visualization Button
        visualize_button = tk.Button(root, text="Visualize Shape", command=self.visualize_shape)
        visualize_button.pack(pady=5)


        # Quiz Section
        quiz_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        quiz_button.pack(pady=10)

        # Answer Frame
        self.answer_frame = tk.Frame(root)
        self.answer_label = tk.Label(self.answer_frame, text="Your Answer:")
        self.answer_label.pack(side=tk.LEFT)
        self.answer_entry = tk.Entry(self.answer_frame, width=20)
        self.answer_entry.pack(side=tk.LEFT, padx=5)
        self.answer_submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_quiz_answer)
        self.answer_submit_button.pack(side=tk.LEFT)
        self.answer_frame.pack(pady=10)

        # Text Display Area
        self.text_area = tk.Text(root, wrap=tk.WORD, height=25, width=80)
        self.text_area.pack(pady=20)
        self.text_area.configure(state=tk.DISABLED)


    def get_all_shapes(self):
        """
        Get all shape classes
        """
        three_dim_cls = self.ontology.search_one(iri="*ThreeDimensionalShape")
        two_dim_cls = self.ontology.search_one(iri="*TwoDimensionalShape")

        all_cls = list(three_dim_cls.subclasses()) + list(two_dim_cls.subclasses())
        return all_cls

    def show_all_shapes(self):
        """
        Display subclasses of all shapes
        """
    
        all_shape_classes = self.get_all_shapes()

        if not all_shape_classes:
            result = "No shape found."
            self.display_text(result)
            return 

        subclasses = [subclass.name for subclass in all_shape_classes]
        result = f"List of the available shapes:\n" + "\n".join(f"  - {name}" for name in subclasses)
        self.display_text(result)


    def show_3d_subclasses(self):
        """
        Display subclasses of ThreeDimensionalShape.
        """
        result = list_subclasses(self.ontology, "ThreeDimensionalShape")
        self.display_text(result)

    def show_2d_subclasses(self):
        """
        Display subclasses of TwoDimensionalShape.
        """
        result = list_subclasses(self.ontology, "TwoDimensionalShape")
        self.display_text(result)

    def search_shape_details(self):
        """
        Search for shape details based on user input.
        """
        shape_name = self.search_entry.get().strip()
        if not shape_name:
            messagebox.showwarning("Input Error", "Please enter a shape name.")
            return
        details = search_shape(self.ontology, shape_name, for_quiz=False)
        if not details:
            messagebox.showinfo("Search Result", f"No shape found with the name '{shape_name}'.")
        else:
            self.display_text(details)

    def start_quiz(self):
        """
        Start a new quiz round by selecting a random shape.
        """
        shapes = self.get_all_shapes()

        if not shapes:
            messagebox.showerror("Error", "No shapes found in the ontology.")
            return
        self.current_quiz_shape = random.choice(shapes)
        details = search_shape(self.ontology, self.current_quiz_shape.name, for_quiz=True)
        if details:
            quiz_text = "Guess the Shape!\n\n" + details
            self.display_text(quiz_text)

    def submit_quiz_answer(self):
        """
        Check the user's answer to the quiz question.
        """
        if not self.current_quiz_shape:
            messagebox.showerror("Quiz Error", "No active quiz round. Start a new quiz.")
            return
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == self.current_quiz_shape.name.lower():
            messagebox.showinfo("Quiz Result", "Correct! Well done.")
        else:
            messagebox.showinfo("Quiz Result", f"Wrong! The correct answer is '{self.current_quiz_shape.name}'.")
        self.answer_entry.delete(0, tk.END)
        self.current_quiz_shape = None

    def visualize_shape(self):
        shape_name = self.search_entry.get().strip()
        if not shape_name:
            messagebox.showwarning("Input Error", "Please enter a shape name.")
            return
        visualize_shape(shape_name)

    def display_text(self, content: str):
        """
        Display the given content in the text area.
        """
        self.text_area.configure(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, content)
        self.text_area.configure(state=tk.DISABLED)


def main():
    """
    Main function to load ontology and launch the application.
    """
    file_path = "aic2.rdf"  # Path to the ontology file
    ontology = load_ontology(file_path)
    if ontology is None:
        return

    root = tk.Tk()
    app = OntologyApp(root, ontology)
    root.mainloop()


if __name__ == "__main__":
    main()