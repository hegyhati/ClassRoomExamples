package rpg.view;

import rpg.model.GameStateViewer;
import rpg.presenter.Presenter;

import java.awt.Dimension;
import java.awt.Image;
import javax.swing.*;

class MapPanel extends ViewPanel{
    private final int visibilityRange;
    private final int size;
    private final int tileSize;
    private final JLabel[][] mapView;
    private final ImageIcon WALL_ICON, FREE_ICON, MONSTER_ICON, HERO_ICON, HERO_MONSTER_ICON; 

    private ImageIcon getScaledTile(String file) {
        return new ImageIcon(new ImageIcon("resources/tiles/" + file).getImage().getScaledInstance(tileSize, tileSize, Image.SCALE_SMOOTH));
    }

    MapPanel(Presenter presenter, GameStateViewer model, int size, int visibilityRange) {
        super(presenter, model);

        this.visibilityRange = visibilityRange;
        this.size = size;
        this.tileSize  = size / (2*visibilityRange+1);
        this.mapView = new JLabel[2*visibilityRange+1][2*visibilityRange+1];
        this.WALL_ICON = getScaledTile("wall.png");
        this.FREE_ICON = getScaledTile("free.png");
        this.MONSTER_ICON = getScaledTile("monster.png");
        this.HERO_ICON = getScaledTile("hero.png");
        this.HERO_MONSTER_ICON = getScaledTile("heromonster.png");

        setLayout(null);
        for (int row = 0; row <  2 * this.visibilityRange + 1 ; ++row)
            for (int col = 0; col < 2 * this.visibilityRange + 1; ++col) {
                JLabel tile = new JLabel();
                tile.setBounds(tileSize*col,tileSize*row, tileSize, tileSize);
                this.mapView[row][col] = tile;
                add(tile);
            }
        setPreferredSize(new Dimension(size,size));

        updateView();
    }

    @Override
    public void updateView() {
         for (int row=-visibilityRange; row <= visibilityRange; ++row)
            for (int col = -visibilityRange; col <= visibilityRange; ++col) 
                this.mapView[row+visibilityRange][col+visibilityRange].setIcon(
                    this.model.isWall(row, col)
                    ? WALL_ICON 
                    : row == 0 && col == 0 && this.model.getHero().isAlive()
                        ? this.model.hasMonster(row, col) ? HERO_MONSTER_ICON : HERO_ICON
                        : this.model.hasMonster(row, col) ? MONSTER_ICON : FREE_ICON
                );
    }
}