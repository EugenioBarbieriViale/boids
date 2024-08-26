#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <raylib.h>

#define W 1000
#define H 800

#define N 1
#define size 30

typedef struct {
    Vector2 pos;
    float vel;
    float angle;
} Boid;

void init_flock(Boid flock[]) {
    float angles[10];
    for (int i=0; i<N; i++) {
        angles[i] = (float)i/20;
    }

    for (int i=0; i<N; i++) {
        flock[i].pos = (Vector2){i*30+200, 300};
        flock[i].angle = angles[rand() % N];
    }
}

Vector2 rotate(Vector2 pos, float a) {
    float new_x = (pos.x * cos(a) - pos.y * sin(a));
    float new_y = (pos.x * sin(a) + pos.y * cos(a));
    return (Vector2){new_x, new_y};
}

void draw_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        Vector2 pos = flock[i].pos;
        /* float a = flock[i].angle; */
        float a = PI/6;

        Vector2 d1 = rotate((Vector2){-size, size}, a);
        Vector2 d2 = rotate((Vector2){size, size}, a);
        Vector2 d3 = rotate((Vector2){size, -size}, a);

        Vector2 v1 = (Vector2){pos.x + d1.x, pos.y + d1.y};
        Vector2 v2 = (Vector2){pos.x + d2.x, pos.y + d2.y};
        Vector2 v3 = (Vector2){pos.x + d3.x, pos.y + d3.y};

        DrawTriangle(v1, v2, v3, RED);
        DrawRectangleV(v1, (Vector2){5,5}, YELLOW);
        /* DrawRectangleV(v2, (Vector2){5,5}, BLUE); */
        /* DrawRectangleV(v3, (Vector2){5,5}, GREEN); */
    }
}

int main() {
    InitWindow(W, H, "Boids");
    SetTargetFPS(30);

    Boid flock[N];
    init_flock(flock);

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(GRAY);

        draw_flock(flock);

        EndDrawing();

    }

    return 0;
}
