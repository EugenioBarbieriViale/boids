#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <raylib.h>

#define W 1000
#define H 800

#define N 30
#define size 30

#define square(x) (x)*(x)

typedef struct {
    Vector2 pos;
    Vector2 vel;
    float angle;
} Boid;

float distance(Vector2 v1, Vector2 v2) {
    return (float)(sqrt(square(v1.x - v2.x) + square(v1.y - v2.y)));
}

float rand_angle() {
    return (float)rand() / (float)RAND_MAX * (2*PI);
}

Vector2 move(Vector2 pos, Vector2 vel) {
    pos.x += vel.x;
    pos.y += vel.y;
    return pos;
}

void init_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        flock[i].pos = (Vector2){rand() % W, rand() % H};
        flock[i].angle = rand_angle();
        float v_magn = rand() % 4+0.4;
        flock[i].vel = (Vector2){v_magn*sin(flock[i].angle), v_magn*cos(flock[i].angle)};
    }
}

void separation(Boid b, Boid flock[]) {
    for (int i=0; i<N; i++) {
        float d = distance(b.pos, flock[i].pos);
        if (d <= 50) {
            printf("%f\n", d);
        }
    }
}

void draw_flock(Boid flock[]) {
    for (int i=0; i<N; i++) {
        Vector2 pos = flock[i].pos;
        Vector2 vel = flock[i].vel;
        float a = flock[i].angle-PI/2;

        Vector2 v1 = (Vector2){pos.x + size*cos(a), pos.y - size*sin(a)};
        Vector2 v2 = (Vector2){pos.x - size*sin(a)/2, pos.y - size*cos(a)/2};
        Vector2 v3 = (Vector2){pos.x + size*sin(a)/2, pos.y + size*cos(a)/2};

        /* DrawCircleV(pos, 50, YELLOW); */
        DrawTriangle(v1, v2, v3, GRAY);

        flock[i].pos = move(pos, vel);
    }
}

int main() {
    srand(time(NULL));

    InitWindow(W, H, "Boids");
    SetTargetFPS(30);

    Boid flock[N];
    init_flock(flock);

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(BLACK);

        for (int i=0; i<N; i++) {
            separation(flock[i], flock);
        }
        draw_flock(flock);

        EndDrawing();

    }

    return 0;
}
