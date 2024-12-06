mod components;
use components::Navbar;
use sycamore::prelude::*;

#[component]
fn App() -> View {
    view! {
        Navbar()
        div {
            h1(id="hello-id") { "Hello world from h1 tag"}
            p { "Hello world from p tag"}
        }
    }
}

fn main() {
    sycamore::render(App)
}
